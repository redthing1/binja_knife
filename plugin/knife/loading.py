from __future__ import annotations

from typing import Any

from .sessions import SessionError

VIEW_METADATA = "knife.view_type"


class ViewLoader:
    def __init__(self, bn: Any) -> None:
        self.bn = bn

    def __call__(self, path: str, *, update_analysis: bool = True,
                 view_type: str | None = None, list_views: bool = False) -> Any:
        view = self.bn.load(path, update_analysis=False)
        if view is None:
            raise SessionError(f"Binary Ninja could not open {path}", kind="load")
        try:
            saved = bool(view.file.has_database)
            choices = sorted(set(view.file.existing_views if saved else
                                 [item.name for item in view.file.raw.available_view_types]))
            if list_views:
                view.file.close()
                return {"views": choices}
            if view_type is None and saved:
                try:
                    view_type = view.file.raw.query_metadata(VIEW_METADATA)
                except KeyError:
                    pass
                if view_type is not None and not isinstance(view_type, str):
                    raise SessionError("database has an invalid selected view", kind="view")
            meaningful = [name for name in choices if name not in {"Raw", "Mapped"}]
            if view_type is None:
                if len(meaningful) > 1:
                    raise SessionError("several views apply; choose --view: " + ", ".join(meaningful),
                                       kind="view", details={"views": choices})
                view_type = meaningful[0] if meaningful else view.view_type
            if view_type not in choices:
                raise SessionError(f"view '{view_type}' is unavailable; choices: {', '.join(choices)}",
                                   kind="view", details={"views": choices})
            try:
                selected = view.file.get_view_of_type(view_type)
            except (KeyError, ValueError) as error:
                raise SessionError(f"could not load view '{view_type}'; check its plugin", kind="view") from error
            if selected is None or selected.view_type != view_type:
                raise SessionError(f"could not load view '{view_type}'; check its plugin", kind="view")
            if update_analysis:
                selected.update_analysis_and_wait()
            return selected
        except BaseException:
            view.file.close()
            raise
