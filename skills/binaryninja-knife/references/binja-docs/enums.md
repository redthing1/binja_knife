# enums module

| Class | Description |
| --- | --- |
| [`binaryninja.enums.ActionType`](#binaryninja.enums.ActionType "binaryninja.enums.ActionType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.AnalysisMode`](#binaryninja.enums.AnalysisMode "binaryninja.enums.AnalysisMode") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.AnalysisSkipReason`](#binaryninja.enums.AnalysisSkipReason "binaryninja.enums.AnalysisSkipReason") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.AnalysisState`](#binaryninja.enums.AnalysisState "binaryninja.enums.AnalysisState") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.AnalysisWarningActionType`](#binaryninja.enums.AnalysisWarningActionType "binaryninja.enums.AnalysisWarningActionType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.BaseAddressDetectionAnalysisMode`](#binaryninja.enums.BaseAddressDetectionAnalysisMode "binaryninja.enums.BaseAddressDetectionAnalysisMode") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.BaseAddressDetectionConfidence`](#binaryninja.enums.BaseAddressDetectionConfidence "binaryninja.enums.BaseAddressDetectionConfidence") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.BaseAddressDetectionPOISetting`](#binaryninja.enums.BaseAddressDetectionPOISetting "binaryninja.enums.BaseAddressDetectionPOISetting") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.BaseAddressDetectionPOIType`](#binaryninja.enums.BaseAddressDetectionPOIType "binaryninja.enums.BaseAddressDetectionPOIType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.BinaryViewEventType`](#binaryninja.enums.BinaryViewEventType "binaryninja.enums.BinaryViewEventType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.BraceRequirement`](#binaryninja.enums.BraceRequirement "binaryninja.enums.BraceRequirement") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.BranchType`](#binaryninja.enums.BranchType "binaryninja.enums.BranchType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.BuiltinType`](#binaryninja.enums.BuiltinType "binaryninja.enums.BuiltinType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.CallingConventionName`](#binaryninja.enums.CallingConventionName "binaryninja.enums.CallingConventionName") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.CollaborationPermissionLevel`](#binaryninja.enums.CollaborationPermissionLevel "binaryninja.enums.CollaborationPermissionLevel") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.DataFlowQueryOption`](#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.DeadStoreElimination`](#binaryninja.enums.DeadStoreElimination "binaryninja.enums.DeadStoreElimination") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.DerivedStringLocationType`](#binaryninja.enums.DerivedStringLocationType "binaryninja.enums.DerivedStringLocationType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.DisassemblyAddressMode`](#binaryninja.enums.DisassemblyAddressMode "binaryninja.enums.DisassemblyAddressMode") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.DisassemblyBlockLabels`](#binaryninja.enums.DisassemblyBlockLabels "binaryninja.enums.DisassemblyBlockLabels") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.DisassemblyCallParameterHints`](#binaryninja.enums.DisassemblyCallParameterHints "binaryninja.enums.DisassemblyCallParameterHints") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.DisassemblyOption`](#binaryninja.enums.DisassemblyOption "binaryninja.enums.DisassemblyOption") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.EarlyReturn`](#binaryninja.enums.EarlyReturn "binaryninja.enums.EarlyReturn") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.EdgePenStyle`](#binaryninja.enums.EdgePenStyle "binaryninja.enums.EdgePenStyle") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.Endianness`](#binaryninja.enums.Endianness "binaryninja.enums.Endianness") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ExprFolding`](#binaryninja.enums.ExprFolding "binaryninja.enums.ExprFolding") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FindFlag`](#binaryninja.enums.FindFlag "binaryninja.enums.FindFlag") | Support for integer-based Flags |
| [`binaryninja.enums.FindRangeType`](#binaryninja.enums.FindRangeType "binaryninja.enums.FindRangeType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FindType`](#binaryninja.enums.FindType "binaryninja.enums.FindType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FirmwareNinjaMemoryAccessType`](#binaryninja.enums.FirmwareNinjaMemoryAccessType "binaryninja.enums.FirmwareNinjaMemoryAccessType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FirmwareNinjaMemoryHeuristic`](#binaryninja.enums.FirmwareNinjaMemoryHeuristic "binaryninja.enums.FirmwareNinjaMemoryHeuristic") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FirmwareNinjaSectionAnalysisMode`](#binaryninja.enums.FirmwareNinjaSectionAnalysisMode "binaryninja.enums.FirmwareNinjaSectionAnalysisMode") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FirmwareNinjaSectionType`](#binaryninja.enums.FirmwareNinjaSectionType "binaryninja.enums.FirmwareNinjaSectionType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FlagRole`](#binaryninja.enums.FlagRole "binaryninja.enums.FlagRole") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FlowGraphOption`](#binaryninja.enums.FlowGraphOption "binaryninja.enums.FlowGraphOption") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ForceVersionReason`](#binaryninja.enums.ForceVersionReason "binaryninja.enums.ForceVersionReason") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FormInputFieldType`](#binaryninja.enums.FormInputFieldType "binaryninja.enums.FormInputFieldType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FunctionAnalysisSkipOverride`](#binaryninja.enums.FunctionAnalysisSkipOverride "binaryninja.enums.FunctionAnalysisSkipOverride") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FunctionGraphType`](#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.FunctionUpdateType`](#binaryninja.enums.FunctionUpdateType "binaryninja.enums.FunctionUpdateType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.HighLevelILOperation`](#binaryninja.enums.HighLevelILOperation "binaryninja.enums.HighLevelILOperation") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.HighlightColorStyle`](#binaryninja.enums.HighlightColorStyle "binaryninja.enums.HighlightColorStyle") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.HighlightStandardColor`](#binaryninja.enums.HighlightStandardColor "binaryninja.enums.HighlightStandardColor") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ILBranchDependence`](#binaryninja.enums.ILBranchDependence "binaryninja.enums.ILBranchDependence") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ILInstructionAttribute`](#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute") | Support for integer-based Flags |
| [`binaryninja.enums.ImplicitRegisterExtend`](#binaryninja.enums.ImplicitRegisterExtend "binaryninja.enums.ImplicitRegisterExtend") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.InlineDuringAnalysis`](#binaryninja.enums.InlineDuringAnalysis "binaryninja.enums.InlineDuringAnalysis") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.InstructionTextTokenContext`](#binaryninja.enums.InstructionTextTokenContext "binaryninja.enums.InstructionTextTokenContext") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.InstructionTextTokenType`](#binaryninja.enums.InstructionTextTokenType "binaryninja.enums.InstructionTextTokenType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.IntegerDisplayType`](#binaryninja.enums.IntegerDisplayType "binaryninja.enums.IntegerDisplayType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.IntrinsicClass`](#binaryninja.enums.IntrinsicClass "binaryninja.enums.IntrinsicClass") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.LinearDisassemblyLineType`](#binaryninja.enums.LinearDisassemblyLineType "binaryninja.enums.LinearDisassemblyLineType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.LinearSweepAnalysisCapability`](#binaryninja.enums.LinearSweepAnalysisCapability "binaryninja.enums.LinearSweepAnalysisCapability") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.LinearViewObjectIdentifierType`](#binaryninja.enums.LinearViewObjectIdentifierType "binaryninja.enums.LinearViewObjectIdentifierType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.LogLevel`](#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.LowLevelILFlagCondition`](#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.LowLevelILOperation`](#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.MediumLevelILOperation`](#binaryninja.enums.MediumLevelILOperation "binaryninja.enums.MediumLevelILOperation") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.MemberAccess`](#binaryninja.enums.MemberAccess "binaryninja.enums.MemberAccess") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.MemberScope`](#binaryninja.enums.MemberScope "binaryninja.enums.MemberScope") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.MergeConflictDataType`](#binaryninja.enums.MergeConflictDataType "binaryninja.enums.MergeConflictDataType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.MessageBoxButtonResult`](#binaryninja.enums.MessageBoxButtonResult "binaryninja.enums.MessageBoxButtonResult") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.MessageBoxButtonSet`](#binaryninja.enums.MessageBoxButtonSet "binaryninja.enums.MessageBoxButtonSet") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.MessageBoxIcon`](#binaryninja.enums.MessageBoxIcon "binaryninja.enums.MessageBoxIcon") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.MetadataStoreFlag`](#binaryninja.enums.MetadataStoreFlag "binaryninja.enums.MetadataStoreFlag") | Support for integer-based Flags |
| [`binaryninja.enums.MetadataType`](#binaryninja.enums.MetadataType "binaryninja.enums.MetadataType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ModificationStatus`](#binaryninja.enums.ModificationStatus "binaryninja.enums.ModificationStatus") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.NameType`](#binaryninja.enums.NameType "binaryninja.enums.NameType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.NamedTypeReferenceClass`](#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.OperatorPrecedence`](#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.PluginCommandType`](#binaryninja.enums.PluginCommandType "binaryninja.enums.PluginCommandType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.PluginDependencyConflictStatus`](#binaryninja.enums.PluginDependencyConflictStatus "binaryninja.enums.PluginDependencyConflictStatus") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.PluginDependencyDecision`](#binaryninja.enums.PluginDependencyDecision "binaryninja.enums.PluginDependencyDecision") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.PluginLoadPhase`](#binaryninja.enums.PluginLoadPhase "binaryninja.enums.PluginLoadPhase") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.PluginLoadStatus`](#binaryninja.enums.PluginLoadStatus "binaryninja.enums.PluginLoadStatus") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.PluginOrigin`](#binaryninja.enums.PluginOrigin "binaryninja.enums.PluginOrigin") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.PluginStatus`](#binaryninja.enums.PluginStatus "binaryninja.enums.PluginStatus") | Support for integer-based Flags |
| [`binaryninja.enums.PluginType`](#binaryninja.enums.PluginType "binaryninja.enums.PluginType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.PointerBaseType`](#binaryninja.enums.PointerBaseType "binaryninja.enums.PointerBaseType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.PointerSuffix`](#binaryninja.enums.PointerSuffix "binaryninja.enums.PointerSuffix") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ReferenceType`](#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.RegisterValueType`](#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.RelocationType`](#binaryninja.enums.RelocationType "binaryninja.enums.RelocationType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.RemoteFileType`](#binaryninja.enums.RemoteFileType "binaryninja.enums.RemoteFileType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.RenderLayerDefaultEnableState`](#binaryninja.enums.RenderLayerDefaultEnableState "binaryninja.enums.RenderLayerDefaultEnableState") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ReportType`](#binaryninja.enums.ReportType "binaryninja.enums.ReportType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SaveOption`](#binaryninja.enums.SaveOption "binaryninja.enums.SaveOption") | Support for integer-based Flags |
| [`binaryninja.enums.ScopeType`](#binaryninja.enums.ScopeType "binaryninja.enums.ScopeType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ScriptingProviderExecuteResult`](#binaryninja.enums.ScriptingProviderExecuteResult "binaryninja.enums.ScriptingProviderExecuteResult") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ScriptingProviderInputReadyState`](#binaryninja.enums.ScriptingProviderInputReadyState "binaryninja.enums.ScriptingProviderInputReadyState") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SectionSemantics`](#binaryninja.enums.SectionSemantics "binaryninja.enums.SectionSemantics") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SegmentFlag`](#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag") | Support for integer-based Flags |
| [`binaryninja.enums.SettingsScope`](#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") | Support for integer-based Flags |
| [`binaryninja.enums.SimilarityAnnotationType`](#binaryninja.enums.SimilarityAnnotationType "binaryninja.enums.SimilarityAnnotationType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SimilarityApplyStatus`](#binaryninja.enums.SimilarityApplyStatus "binaryninja.enums.SimilarityApplyStatus") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SimilarityEntityType`](#binaryninja.enums.SimilarityEntityType "binaryninja.enums.SimilarityEntityType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SimilarityViewType`](#binaryninja.enums.SimilarityViewType "binaryninja.enums.SimilarityViewType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.StringType`](#binaryninja.enums.StringType "binaryninja.enums.StringType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.StructureVariant`](#binaryninja.enums.StructureVariant "binaryninja.enums.StructureVariant") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SwitchRecovery`](#binaryninja.enums.SwitchRecovery "binaryninja.enums.SwitchRecovery") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SymbolBinding`](#binaryninja.enums.SymbolBinding "binaryninja.enums.SymbolBinding") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SymbolDisplayResult`](#binaryninja.enums.SymbolDisplayResult "binaryninja.enums.SymbolDisplayResult") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SymbolDisplayType`](#binaryninja.enums.SymbolDisplayType "binaryninja.enums.SymbolDisplayType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SymbolType`](#binaryninja.enums.SymbolType "binaryninja.enums.SymbolType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.SyncStatus`](#binaryninja.enums.SyncStatus "binaryninja.enums.SyncStatus") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TagReferenceType`](#binaryninja.enums.TagReferenceType "binaryninja.enums.TagReferenceType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TagTypeType`](#binaryninja.enums.TagTypeType "binaryninja.enums.TagTypeType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ThemeColor`](#binaryninja.enums.ThemeColor "binaryninja.enums.ThemeColor") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TokenEscapingType`](#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TransformCapabilities`](#binaryninja.enums.TransformCapabilities "binaryninja.enums.TransformCapabilities") | Support for integer-based Flags |
| [`binaryninja.enums.TransformResult`](#binaryninja.enums.TransformResult "binaryninja.enums.TransformResult") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TransformSessionMode`](#binaryninja.enums.TransformSessionMode "binaryninja.enums.TransformSessionMode") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TransformType`](#binaryninja.enums.TransformType "binaryninja.enums.TransformType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TypeClass`](#binaryninja.enums.TypeClass "binaryninja.enums.TypeClass") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TypeContainerType`](#binaryninja.enums.TypeContainerType "binaryninja.enums.TypeContainerType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TypeDefinitionLineType`](#binaryninja.enums.TypeDefinitionLineType "binaryninja.enums.TypeDefinitionLineType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TypeParserErrorSeverity`](#binaryninja.enums.TypeParserErrorSeverity "binaryninja.enums.TypeParserErrorSeverity") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TypeParserOption`](#binaryninja.enums.TypeParserOption "binaryninja.enums.TypeParserOption") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.TypeReferenceType`](#binaryninja.enums.TypeReferenceType "binaryninja.enums.TypeReferenceType") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.UpdateResult`](#binaryninja.enums.UpdateResult "binaryninja.enums.UpdateResult") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.ValueLocationSource`](#binaryninja.enums.ValueLocationSource "binaryninja.enums.ValueLocationSource") | Enum where members are also (and must be) ints |
| [`binaryninja.enums.VariableSourceType`](#binaryninja.enums.VariableSourceType "binaryninja.enums.VariableSourceType") | Enum where members are also (and must be) ints |

## ActionType

*class* ActionType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ActionType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AnalysisAction *= 2*

    DataModificationAction *= 1*

    DataModificationAndAnalysisAction *= 3*

    TemporaryAction *= 0*

## AnalysisMode

*class* AnalysisMode[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#AnalysisMode)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BasicAnalysisMode *= 2*

    ControlFlowAnalysisMode *= 3*

    FullAnalysisMode *= 0*

    IntermediateAnalysisMode *= 1*

## AnalysisSkipReason

*class* AnalysisSkipReason[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#AnalysisSkipReason)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AlwaysSkipReason *= 1*

    AnalysisPipelineSuspendedReason *= 8*

    BasicAnalysisSkipReason *= 6*

    ExceedFunctionAnalysisTimeSkipReason *= 3*

    ExceedFunctionSizeSkipReason *= 2*

    ExceedFunctionUpdateCountSkipReason *= 4*

    IntermediateAnalysisSkipReason *= 7*

    NewAutoFunctionAnalysisSuppressedReason *= 5*

    NoSkipReason *= 0*

## AnalysisState

*class* AnalysisState[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#AnalysisState)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AnalyzeState *= 5*

    DisassembleState *= 4*

    DiscoveryState *= 3*

    ExtendedAnalyzeState *= 6*

    HoldState *= 1*

    IdleState *= 2*

    InitialState *= 0*

## AnalysisWarningActionType

*class* AnalysisWarningActionType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#AnalysisWarningActionType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DisableGuidedAnalysisWarningAction *= 3*

    ForceAnalysisWarningAction *= 1*

    NoAnalysisWarningAction *= 0*

    ShowStackGraphWarningAction *= 2*

## BaseAddressDetectionAnalysisMode

*class* BaseAddressDetectionAnalysisMode[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BaseAddressDetectionAnalysisMode)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    InstructionAnalysisBaseAddressDetection *= 0*

    SamplingBaseAddressDetection *= 1*

## BaseAddressDetectionConfidence

*class* BaseAddressDetectionConfidence[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BaseAddressDetectionConfidence)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    HighConfidence *= 2*

    LowConfidence *= 1*

    NoConfidence *= 0*

## BaseAddressDetectionPOISetting

*class* BaseAddressDetectionPOISetting[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BaseAddressDetectionPOISetting)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    POIAnalysisAll *= 2*

    POIAnalysisFunctionsOnly *= 1*

    POIAnalysisStringsOnly *= 0*

## BaseAddressDetectionPOIType

*class* BaseAddressDetectionPOIType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BaseAddressDetectionPOIType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    POIDataVariable *= 2*

    POIFileEnd *= 4*

    POIFileStart *= 3*

    POIFunction *= 1*

    POIString *= 0*

## BinaryViewEventType

*class* BinaryViewEventType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BinaryViewEventType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BinaryViewFinalizationEvent *= 0*

    BinaryViewInitialAnalysisCompletionEvent *= 1*

## BraceRequirement

*class* BraceRequirement[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BraceRequirement)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BracesAlwaysRequired *= 2*

    BracesNotAllowed *= 1*

    OptionalBraces *= 0*

## BranchType

*class* BranchType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BranchType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CallDestination *= 3*

    ExceptionBranch *= 7*

    FalseBranch *= 1*

    FunctionReturn *= 4*

    IndirectBranch *= 6*

    SystemCall *= 5*

    TrueBranch *= 2*

    UnconditionalBranch *= 0*

    UnresolvedBranch *= 127*

    UserDefinedBranch *= 128*

## BuiltinType

*class* BuiltinType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BuiltinType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BuiltinMemcpy *= 1*

    BuiltinMemset *= 2*

    BuiltinNone *= 0*

    BuiltinStrcpy *= 4*

    BuiltinStrncpy *= 3*

    BuiltinWcscpy *= 5*

    BuiltinWmemcpy *= 6*

## CallingConventionName

*class* CallingConventionName[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#CallingConventionName)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CLRCallCallingConvention *= 6*

    CdeclCallingConvention *= 1*

    EabiCallCallingConvention *= 7*

    FastcallCallingConvention *= 5*

    NoCallingConvention *= 0*

    PascalCallingConvention *= 2*

    STDCallCallingConvention *= 4*

    SwiftAsyncCallingConvention *= 10*

    SwiftCallingConvention *= 9*

    ThisCallCallingConvention *= 3*

    VectorCallCallingConvention *= 8*

## CollaborationPermissionLevel

*class* CollaborationPermissionLevel[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#CollaborationPermissionLevel)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AdminPermission *= 1*

    EditPermission *= 2*

    ViewPermission *= 3*

## DataFlowQueryOption

*class* DataFlowQueryOption[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DataFlowQueryOption)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AllowReadingWritableMemoryQueryOption *= 1*

    FromAddressesInLookupTableQueryOption *= 0*

## DeadStoreElimination

*class* DeadStoreElimination[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DeadStoreElimination)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AllowDeadStoreElimination *= 2*

    DefaultDeadStoreElimination *= 0*

    PreventDeadStoreElimination *= 1*

## DerivedStringLocationType

*class* DerivedStringLocationType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DerivedStringLocationType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CodeStringLocation *= 1*

    DataBackedStringLocation *= 0*

## DisassemblyAddressMode

*class* DisassemblyAddressMode[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DisassemblyAddressMode)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AbsoluteDisassemblyAddressMode *= 0*

    DecimalDisassemblyAddressModeFlag *= 131072*

    DisassemblyAddressModeFlagsMask *= 4294901760*

    DisassemblyAddressModeMask *= 65535*

    IncludeNameDisassemblyAddressModeFlag *= 65536*

    RelativeToAddressBaseOffsetDisassemblyAddressMode *= 5*

    RelativeToBinaryStartDisassemblyAddressMode *= 1*

    RelativeToDataStartDisassemblyAddressMode *= 6*

    RelativeToFunctionStartDisassemblyAddressMode *= 4*

    RelativeToSectionStartDisassemblyAddressMode *= 3*

    RelativeToSegmentStartDisassemblyAddressMode *= 2*

## DisassemblyBlockLabels

*class* DisassemblyBlockLabels[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DisassemblyBlockLabels)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AlwaysShowBlockLabels *= 1*

    NeverShowBlockLabels *= 2*

    NeverShowDefaultBlockLabels *= 0*

## DisassemblyCallParameterHints

*class* DisassemblyCallParameterHints[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DisassemblyCallParameterHints)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AlwaysShowParameterHints *= 1*

    NeverShowMatchingParameterHints *= 0*

    NeverShowParameterHints *= 2*

## DisassemblyOption

*class* DisassemblyOption[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DisassemblyOption)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DisableLineFormatting *= 68*

    ExpandLongOpcode *= 2*

    GroupLinearDisassemblyFunctions *= 64*

    HighLevelILLinearDisassembly *= 65*

    IndentHLILBody *= 67*

    ShowAddress *= 0*

    ShowCollapseIndicators *= 132*

    ShowFlagUsage *= 128*

    ShowFunctionAddress *= 8*

    ShowFunctionHeader *= 9*

    ShowILOpcodes *= 131*

    ShowILTypes *= 130*

    ShowOpcode *= 1*

    ShowRegisterHighlight *= 7*

    ShowStackPointer *= 129*

    ShowTypeCasts *= 10*

    ShowVariableTypesWhenAssigned *= 4*

    ShowVariablesAtTopOfGraph *= 3*

    WaitForIL *= 66*

## EarlyReturn

*class* EarlyReturn[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#EarlyReturn)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DefaultEarlyReturn *= 0*

    FalseSideEarlyReturn *= 4*

    PreventEarlyReturn *= 1*

    SmallestSideEarlyReturn *= 2*

    TrueSideEarlyReturn *= 3*

## EdgePenStyle

*class* EdgePenStyle[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#EdgePenStyle)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DashDotDotLine *= 5*

    DashDotLine *= 4*

    DashLine *= 2*

    DotLine *= 3*

    NoPen *= 0*

    SolidLine *= 1*

## Endianness

*class* Endianness[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#Endianness)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BigEndian *= 1*

    LittleEndian *= 0*

## ExprFolding

*class* ExprFolding[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ExprFolding)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AllowExprFolding *= 2*

    DefaultExprFolding *= 0*

    PreventExprFolding *= 1*

## FindFlag

*class* FindFlag[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FindFlag)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    __new__(*value*)

    FindCaseInsensitive *= 1*

    FindCaseSensitive *= 0*

    FindIgnoreWhitespace *= 2*

## FindRangeType

*class* FindRangeType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FindRangeType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AllRangeType *= 0*

    CurrentFunctionRangeType *= 2*

    CustomRangeType *= 1*

## FindType

*class* FindType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FindType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    FindTypeBytes *= 4*

    FindTypeConstant *= 3*

    FindTypeEscapedString *= 1*

    FindTypeRawString *= 0*

    FindTypeText *= 2*

## FirmwareNinjaMemoryAccessType

*class* FirmwareNinjaMemoryAccessType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FirmwareNinjaMemoryAccessType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    NoMemoryAccessType *= 0*

    ReadMemoryAccessType *= 1*

    WriteMemoryAccessType *= 2*

## FirmwareNinjaMemoryHeuristic

*class* FirmwareNinjaMemoryHeuristic[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FirmwareNinjaMemoryHeuristic)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CallParamOOBPointerMemoryHeuristic *= 6*

    HasReadBarrierMemoryHeuristic *= 1*

    HasWriteBarrierMemoryHeuristic *= 2*

    LoadFromOOBMemoryMemoryHeuristic *= 4*

    NoMemoryHeuristic *= 0*

    RepeatLoadStoreMemoryHeuristic *= 5*

    StoreToOOBMemoryMemoryHeuristic *= 3*

## FirmwareNinjaSectionAnalysisMode

*class* FirmwareNinjaSectionAnalysisMode[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FirmwareNinjaSectionAnalysisMode)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DefaultSectionAnalysisMode *= 0*

    DetectStringsSectionAnalysisMode *= 2*

    IgnorePaddingSectionAnalysisMode *= 1*

## FirmwareNinjaSectionType

*class* FirmwareNinjaSectionType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FirmwareNinjaSectionType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CodeSectionType *= 0*

    CompressionSectionType *= 2*

    DataSectionType *= 1*

    PaddingSectionType *= 3*

## FlagRole

*class* FlagRole[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FlagRole)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CarryFlagRole *= 4*

    CarryFlagWithInvertedSubtractRole *= 11*

    EvenParityFlagRole *= 7*

    HalfCarryFlagRole *= 6*

    NegativeSignFlagRole *= 3*

    OddParityFlagRole *= 8*

    OrderedFlagRole *= 9*

    OverflowFlagRole *= 5*

    PositiveSignFlagRole *= 2*

    SpecialFlagRole *= 0*

    UnorderedFlagRole *= 10*

    ZeroFlagRole *= 1*

## FlowGraphOption

*class* FlowGraphOption[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FlowGraphOption)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    FlowGraphAllowsInlineInstructionEditing *= 4*

    FlowGraphAllowsPatching *= 3*

    FlowGraphIncludesUserComments *= 2*

    FlowGraphIsAddressable *= 6*

    FlowGraphIsWorkflowGraph *= 7*

    FlowGraphShowsSecondaryRegisterHighlighting *= 5*

    FlowGraphUsesBlockHighlights *= 0*

    FlowGraphUsesInstructionHighlights *= 1*

## ForceVersionReason

*class* ForceVersionReason[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ForceVersionReason)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    PartialAccessAnalysisForceVersionReason *= 1*

    UserForceVersionReason *= 0*

## FormInputFieldType

*class* FormInputFieldType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FormInputFieldType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AddressFormField *= 5*

    CheckboxFormField *= 10*

    ChoiceFormField *= 6*

    DirectoryNameFormField *= 9*

    IntegerFormField *= 4*

    LabelFormField *= 0*

    MultilineTextFormField *= 3*

    OpenFileNameFormField *= 7*

    SaveFileNameFormField *= 8*

    SeparatorFormField *= 1*

    TextLineFormField *= 2*

## FunctionAnalysisSkipOverride

*class* FunctionAnalysisSkipOverride[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FunctionAnalysisSkipOverride)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AlwaysSkipFunctionAnalysis *= 2*

    DefaultFunctionAnalysisSkip *= 0*

    NeverSkipFunctionAnalysis *= 1*

## FunctionGraphType

*class* FunctionGraphType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FunctionGraphType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    HighLevelILFunctionGraph *= 8*

    HighLevelILSSAFormFunctionGraph *= 9*

    HighLevelLanguageRepresentationFunctionGraph *= 10*

    InvalidILViewType *= -1*

    LiftedILFunctionGraph *= 2*

    LowLevelILFunctionGraph *= 1*

    LowLevelILSSAFormFunctionGraph *= 3*

    MappedMediumLevelILFunctionGraph *= 6*

    MappedMediumLevelILSSAFormFunctionGraph *= 7*

    MediumLevelILFunctionGraph *= 4*

    MediumLevelILSSAFormFunctionGraph *= 5*

    NormalFunctionGraph *= 0*

## FunctionUpdateType

*class* FunctionUpdateType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FunctionUpdateType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    FullAutoFunctionUpdate *= 1*

    IncrementalAutoFunctionUpdate *= 2*

    UserFunctionUpdate *= 0*

## HighLevelILOperation

*class* HighLevelILOperation[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#HighLevelILOperation)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    HLIL_ABS *= 141*

    HLIL_ADC *= 37*

    HLIL_ADD *= 36*

    HLIL_ADDRESS_OF *= 27*

    HLIL_ADD_OVERFLOW *= 79*

    HLIL_AND *= 40*

    HLIL_ARRAY_INDEX *= 23*

    HLIL_ARRAY_INDEX_SSA *= 123*

    HLIL_ASR *= 45*

    HLIL_ASSERT *= 20*

    HLIL_ASSERT_SSA *= 120*

    HLIL_ASSIGN *= 17*

    HLIL_ASSIGN_MEM_SSA *= 117*

    HLIL_ASSIGN_UNPACK *= 18*

    HLIL_ASSIGN_UNPACK_MEM_SSA *= 118*

    HLIL_BLOCK *= 1*

    HLIL_BOOL_TO_INT *= 78*

    HLIL_BP *= 83*

    HLIL_BREAK *= 8*

    HLIL_BSWAP *= 131*

    HLIL_CALL *= 66*

    HLIL_CALL_SSA *= 126*

    HLIL_CASE *= 7*

    HLIL_CEIL *= 102*

    HLIL_CLS *= 136*

    HLIL_CLZ *= 133*

    HLIL_CMP_E *= 67*

    HLIL_CMP_NE *= 68*

    HLIL_CMP_SGE *= 73*

    HLIL_CMP_SGT *= 75*

    HLIL_CMP_SLE *= 71*

    HLIL_CMP_SLT *= 69*

    HLIL_CMP_UGE *= 74*

    HLIL_CMP_UGT *= 76*

    HLIL_CMP_ULE *= 72*

    HLIL_CMP_ULT *= 70*

    HLIL_CONST *= 30*

    HLIL_CONST_DATA *= 31*

    HLIL_CONST_PTR *= 32*

    HLIL_CONTINUE *= 9*

    HLIL_CTZ *= 134*

    HLIL_DEREF *= 25*

    HLIL_DEREF_FIELD *= 26*

    HLIL_DEREF_FIELD_SSA *= 125*

    HLIL_DEREF_SSA *= 124*

    HLIL_DIVS *= 55*

    HLIL_DIVS_DP *= 56*

    HLIL_DIVU *= 53*

    HLIL_DIVU_DP *= 54*

    HLIL_DO_WHILE *= 4*

    HLIL_DO_WHILE_SSA *= 114*

    HLIL_EXTERN_PTR *= 33*

    HLIL_FABS *= 96*

    HLIL_FADD *= 90*

    HLIL_FCMP_E *= 104*

    HLIL_FCMP_GE *= 108*

    HLIL_FCMP_GT *= 109*

    HLIL_FCMP_LE *= 107*

    HLIL_FCMP_LT *= 106*

    HLIL_FCMP_NE *= 105*

    HLIL_FCMP_O *= 110*

    HLIL_FCMP_UO *= 111*

    HLIL_FDIV *= 93*

    HLIL_FLOAT_CONST *= 34*

    HLIL_FLOAT_CONV *= 99*

    HLIL_FLOAT_TO_INT *= 97*

    HLIL_FLOOR *= 101*

    HLIL_FMUL *= 92*

    HLIL_FNEG *= 95*

    HLIL_FOR *= 5*

    HLIL_FORCE_VER *= 19*

    HLIL_FORCE_VER_SSA *= 119*

    HLIL_FOR_SSA *= 115*

    HLIL_FSQRT *= 94*

    HLIL_FSUB *= 91*

    HLIL_FTRUNC *= 103*

    HLIL_GOTO *= 13*

    HLIL_IF *= 2*

    HLIL_IMPORT *= 35*

    HLIL_INTRINSIC *= 82*

    HLIL_INTRINSIC_SSA *= 128*

    HLIL_INT_TO_FLOAT *= 98*

    HLIL_JUMP *= 10*

    HLIL_LABEL *= 14*

    HLIL_LOW_PART *= 65*

    HLIL_LSL *= 43*

    HLIL_LSR *= 44*

    HLIL_MAXS *= 138*

    HLIL_MAXU *= 140*

    HLIL_MEM_PHI *= 130*

    HLIL_MINS *= 137*

    HLIL_MINU *= 139*

    HLIL_MODS *= 59*

    HLIL_MODS_DP *= 60*

    HLIL_MODU *= 57*

    HLIL_MODU_DP *= 58*

    HLIL_MUL *= 50*

    HLIL_MULS_DP *= 52*

    HLIL_MULU_DP *= 51*

    HLIL_NEG *= 61*

    HLIL_NOP *= 0*

    HLIL_NORET *= 12*

    HLIL_NOT *= 62*

    HLIL_OR *= 41*

    HLIL_PASS_BY_REF *= 28*

    HLIL_POPCNT *= 132*

    HLIL_RBIT *= 135*

    HLIL_RET *= 11*

    HLIL_RETURN_BY_REF *= 29*

    HLIL_RLC *= 47*

    HLIL_ROL *= 46*

    HLIL_ROR *= 48*

    HLIL_ROUND_TO_INT *= 100*

    HLIL_RRC *= 49*

    HLIL_SBB *= 39*

    HLIL_SPLIT *= 24*

    HLIL_STRUCT_FIELD *= 22*

    HLIL_STRUCT_INIT *= 88*

    HLIL_STRUCT_INIT_FIELD *= 89*

    HLIL_SUB *= 38*

    HLIL_SWITCH *= 6*

    HLIL_SX *= 63*

    HLIL_SYSCALL *= 80*

    HLIL_SYSCALL_SSA *= 127*

    HLIL_TAILCALL *= 81*

    HLIL_TEST_BIT *= 77*

    HLIL_TRAP *= 84*

    HLIL_UNDEF *= 85*

    HLIL_UNIMPL *= 86*

    HLIL_UNIMPL_MEM *= 87*

    HLIL_UNREACHABLE *= 112*

    HLIL_VAR *= 21*

    HLIL_VAR_DECLARE *= 15*

    HLIL_VAR_INIT *= 16*

    HLIL_VAR_INIT_SSA *= 116*

    HLIL_VAR_PHI *= 129*

    HLIL_VAR_SSA *= 121*

    HLIL_VAR_SSA_PARTIAL *= 122*

    HLIL_WHILE *= 3*

    HLIL_WHILE_SSA *= 113*

    HLIL_XOR *= 42*

    HLIL_ZX *= 64*

## HighlightColorStyle

*class* HighlightColorStyle[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#HighlightColorStyle)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CustomHighlightColor *= 2*

    MixedHighlightColor *= 1*

    StandardHighlightColor *= 0*

## HighlightStandardColor

*class* HighlightStandardColor[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#HighlightStandardColor)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BlackHighlightColor *= 9*

    BlueHighlightColor *= 1*

    CyanHighlightColor *= 3*

    GreenHighlightColor *= 2*

    MagentaHighlightColor *= 5*

    NoHighlightColor *= 0*

    OrangeHighlightColor *= 7*

    RedHighlightColor *= 4*

    WhiteHighlightColor *= 8*

    YellowHighlightColor *= 6*

## ILBranchDependence

*class* ILBranchDependence[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ILBranchDependence)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    FalseBranchDependent *= 2*

    NotBranchDependent *= 0*

    TrueBranchDependent *= 1*

## ILInstructionAttribute

*class* ILInstructionAttribute[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ILInstructionAttribute)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    __new__(*value*)

    HLILEarlyReturnPossible *= 1024*

    HLILFoldableExpr *= 256*

    HLILInvertableCondition *= 512*

    HLILSwitchRecoveryPossible *= 2048*

    ILAllowDeadStoreElimination *= 1*

    ILIsCFGProtected *= 64*

    ILPreventAliasAnalysis *= 32*

    ILPreventDeadStoreElimination *= 2*

    ILStackReturn *= 16384*

    ILTransparentCopy *= 4096*

    MLILAssumePossibleUse *= 4*

    MLILCallingConventionImplicit *= 8192*

    MLILPossiblyUnusedIntermediate *= 128*

    MLILUnknownSize *= 8*

    SrcInstructionUsesPointerAuth *= 16*

## ImplicitRegisterExtend

*class* ImplicitRegisterExtend[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ImplicitRegisterExtend)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    NoExtend *= 0*

    SignExtendToFullWidth *= 2*

    ZeroExtendToFullWidth *= 1*

## InlineDuringAnalysis

*class* InlineDuringAnalysis[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#InlineDuringAnalysis)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DoNotInlineCall *= 0*

    InlinePreservingTargetInstructionAddresses *= 1*

    InlineUsingCallAddress *= 2*

## InstructionTextTokenContext

*class* InstructionTextTokenContext[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#InstructionTextTokenContext)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ConstDataTokenContext *= 6*

    ConstStringDataTokenContext *= 7*

    ContentCollapsedContext *= 11*

    ContentCollapsiblePadding *= 13*

    ContentExpandedContext *= 12*

    DataVariableTokenContext *= 2*

    DerivedStringReferenceTokenContext *= 14*

    FunctionReturnTokenContext *= 3*

    ILInstructionIndexTokenContext *= 5*

    InstructionAddressTokenContext *= 4*

    LocalVariableTokenContext *= 1*

    NoTokenContext *= 0*

    StringDataVariableTokenContext *= 9*

    StringDisplayTokenContext *= 10*

    StringReferenceTokenContext *= 8*

## InstructionTextTokenType

*class* InstructionTextTokenType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#InstructionTextTokenType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AddressDisplayToken *= 68*

    AddressSeparatorToken *= 72*

    AnnotationToken *= 9*

    ArgumentNameToken *= 11*

    ArrayIndexToken *= 32*

    BaseStructureNameToken *= 37*

    BaseStructureSeparatorToken *= 38*

    BeginMemoryOperandToken *= 6*

    BraceToken *= 39*

    CharacterConstantToken *= 18*

    CodeRelativeAddressToken *= 10*

    CodeSymbolToken *= 64*

    CollapseStateIndicatorToken *= 74*

    CollapsedInformationToken *= 73*

    CommentToken *= 29*

    DataSymbolToken *= 65*

    EndMemoryOperandToken *= 7*

    EnumerationMemberToken *= 35*

    ExternalSymbolToken *= 70*

    FieldNameToken *= 21*

    FloatingPointToken *= 8*

    GotoLabelToken *= 28*

    HexDumpByteValueToken *= 12*

    HexDumpInvalidByteToken *= 14*

    HexDumpSkippedByteToken *= 13*

    HexDumpTextToken *= 15*

    ImportToken *= 67*

    IndentationToken *= 33*

    IndirectImportToken *= 69*

    InstructionToken *= 1*

    IntegerToken *= 4*

    KeywordToken *= 19*

    LocalVariableToken *= 66*

    NameSpaceSeparatorToken *= 23*

    NameSpaceToken *= 22*

    NewLineToken *= 75*

    OpcodeToken *= 16*

    OperandSeparatorToken *= 2*

    OperationToken *= 36*

    PossibleAddressToken *= 5*

    PossibleValueToken *= 30*

    PossibleValueTypeToken *= 31*

    RegisterToken *= 3*

    StackVariableToken *= 71*

    StringToken *= 17*

    StructOffsetByteValueToken *= 26*

    StructOffsetToken *= 25*

    StructureHexDumpTextToken *= 27*

    TagToken *= 24*

    TextToken *= 0*

    TypeNameToken *= 20*

    UnknownMemoryToken *= 34*

    ValueLocationToken *= 40*

## IntegerDisplayType

*class* IntegerDisplayType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#IntegerDisplayType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BinaryDisplayType *= 1*

    CharacterConstantDisplayType *= 8*

    DefaultIntegerDisplayType *= 0*

    DoubleDisplayType *= 11*

    EnumerationDisplayType *= 12*

    FloatDisplayType *= 10*

    InvertedCharacterConstantDisplayType *= 13*

    PointerDisplayType *= 9*

    SignedDecimalDisplayType *= 4*

    SignedHexadecimalDisplayType *= 6*

    SignedOctalDisplayType *= 2*

    UnsignedComplementDecimalDisplayType *= 14*

    UnsignedComplementHexadecimalDisplayType *= 15*

    UnsignedDecimalDisplayType *= 5*

    UnsignedHexadecimalDisplayType *= 7*

    UnsignedOctalDisplayType *= 3*

## IntrinsicClass

*class* IntrinsicClass[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#IntrinsicClass)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    GeneralIntrinsicClass *= 0*

    MemoryIntrinsicClass *= 1*

## LinearDisassemblyLineType

*class* LinearDisassemblyLineType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LinearDisassemblyLineType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AnalysisWarningLineType *= 19*

    BasicLineType *= 1*

    BlankLineType *= 0*

    CodeDisassemblyLineType *= 2*

    CollapsedFunctionEndLineType *= 20*

    DataVariableLineType *= 3*

    FunctionContinuationLineType *= 8*

    FunctionEndLineType *= 11*

    FunctionHeaderEndLineType *= 7*

    FunctionHeaderLineType *= 5*

    FunctionHeaderStartLineType *= 6*

    HexDumpLineType *= 4*

    LocalVariableLineType *= 9*

    LocalVariableListEndLineType *= 10*

    NonContiguousSeparatorLineType *= 18*

    NoteEndLineType *= 14*

    NoteLineType *= 13*

    NoteStartLineType *= 12*

    SectionEndLineType *= 16*

    SectionSeparatorLineType *= 17*

    SectionStartLineType *= 15*

## LinearSweepAnalysisCapability

*class* LinearSweepAnalysisCapability[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LinearSweepAnalysisCapability)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BNLinearSweepCallTargetAnalysis *= 1*

    BNLinearSweepGenericControlFlowAnalysis *= 2*

## LinearViewObjectIdentifierType

*class* LinearViewObjectIdentifierType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LinearViewObjectIdentifierType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AddressLinearViewObject *= 1*

    AddressRangeLinearViewObject *= 2*

    SingleLinearViewObject *= 0*

## LogLevel

*class* LogLevel[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LogLevel)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AlertLog *= 4*

    DebugLog *= 0*

    ErrorLog *= 3*

    InfoLog *= 1*

    WarningLog *= 2*

## LowLevelILFlagCondition

*class* LowLevelILFlagCondition[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LowLevelILFlagCondition)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    LLFC_E *= 0*

    LLFC_FE *= 14*

    LLFC_FGE *= 18*

    LLFC_FGT *= 19*

    LLFC_FLE *= 17*

    LLFC_FLT *= 16*

    LLFC_FNE *= 15*

    LLFC_FO *= 20*

    LLFC_FUO *= 21*

    LLFC_NE *= 1*

    LLFC_NEG *= 10*

    LLFC_NO *= 13*

    LLFC_O *= 12*

    LLFC_POS *= 11*

    LLFC_SGE *= 6*

    LLFC_SGT *= 8*

    LLFC_SLE *= 4*

    LLFC_SLT *= 2*

    LLFC_UGE *= 7*

    LLFC_UGT *= 9*

    LLFC_ULE *= 5*

    LLFC_ULT *= 3*

## LowLevelILOperation

*class* LowLevelILOperation[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LowLevelILOperation)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    LLIL_ABS *= 153*

    LLIL_ADC *= 25*

    LLIL_ADD *= 24*

    LLIL_ADD_OVERFLOW *= 77*

    LLIL_AND *= 28*

    LLIL_ASR *= 33*

    LLIL_ASSERT *= 6*

    LLIL_ASSERT_SSA *= 122*

    LLIL_BOOL_TO_INT *= 76*

    LLIL_BP *= 79*

    LLIL_BSWAP *= 143*

    LLIL_CALL *= 56*

    LLIL_CALL_OUTPUT_SSA *= 131*

    LLIL_CALL_PARAM *= 129*

    LLIL_CALL_SSA *= 126*

    LLIL_CALL_STACK_ADJUST *= 57*

    LLIL_CALL_STACK_SSA *= 130*

    LLIL_CEIL *= 97*

    LLIL_CLS *= 148*

    LLIL_CLZ *= 145*

    LLIL_CMP_E *= 65*

    LLIL_CMP_NE *= 66*

    LLIL_CMP_SGE *= 71*

    LLIL_CMP_SGT *= 73*

    LLIL_CMP_SLE *= 69*

    LLIL_CMP_SLT *= 67*

    LLIL_CMP_UGE *= 72*

    LLIL_CMP_UGT *= 74*

    LLIL_CMP_ULE *= 70*

    LLIL_CMP_ULT *= 68*

    LLIL_CONST *= 18*

    LLIL_CONST_PTR *= 19*

    LLIL_CTZ *= 146*

    LLIL_DIVS *= 43*

    LLIL_DIVS_DP *= 44*

    LLIL_DIVU *= 41*

    LLIL_DIVU_DP *= 42*

    LLIL_EXTERN_PTR *= 20*

    LLIL_FABS *= 91*

    LLIL_FADD *= 85*

    LLIL_FCMP_E *= 99*

    LLIL_FCMP_GE *= 103*

    LLIL_FCMP_GT *= 104*

    LLIL_FCMP_LE *= 102*

    LLIL_FCMP_LT *= 101*

    LLIL_FCMP_NE *= 100*

    LLIL_FCMP_O *= 105*

    LLIL_FCMP_UO *= 106*

    LLIL_FDIV *= 88*

    LLIL_FLAG *= 22*

    LLIL_FLAG_BIT *= 23*

    LLIL_FLAG_BIT_SSA *= 125*

    LLIL_FLAG_COND *= 63*

    LLIL_FLAG_GROUP *= 64*

    LLIL_FLAG_PHI *= 141*

    LLIL_FLAG_SSA *= 124*

    LLIL_FLOAT_CONST *= 21*

    LLIL_FLOAT_CONV *= 94*

    LLIL_FLOAT_TO_INT *= 92*

    LLIL_FLOOR *= 96*

    LLIL_FMUL *= 87*

    LLIL_FNEG *= 90*

    LLIL_FORCE_VER *= 7*

    LLIL_FORCE_VER_SSA *= 123*

    LLIL_FSQRT *= 89*

    LLIL_FSUB *= 86*

    LLIL_FTRUNC *= 98*

    LLIL_GOTO *= 62*

    LLIL_IF *= 61*

    LLIL_INTRINSIC *= 81*

    LLIL_INTRINSIC_SSA *= 137*

    LLIL_INT_TO_FLOAT *= 93*

    LLIL_JUMP *= 54*

    LLIL_JUMP_TO *= 55*

    LLIL_LOAD *= 8*

    LLIL_LOAD_SSA *= 135*

    LLIL_LOW_PART *= 53*

    LLIL_LSL *= 31*

    LLIL_LSR *= 32*

    LLIL_MAXS *= 150*

    LLIL_MAXU *= 152*

    LLIL_MEMORY_INTRINSIC_OUTPUT_SSA *= 134*

    LLIL_MEMORY_INTRINSIC_SSA *= 138*

    LLIL_MEM_PHI *= 142*

    LLIL_MINS *= 149*

    LLIL_MINU *= 151*

    LLIL_MODS *= 47*

    LLIL_MODS_DP *= 48*

    LLIL_MODU *= 45*

    LLIL_MODU_DP *= 46*

    LLIL_MUL *= 38*

    LLIL_MULS_DP *= 40*

    LLIL_MULU_DP *= 39*

    LLIL_NEG *= 49*

    LLIL_NOP *= 0*

    LLIL_NORET *= 60*

    LLIL_NOT *= 50*

    LLIL_OR *= 29*

    LLIL_POP *= 11*

    LLIL_POPCNT *= 144*

    LLIL_PUSH *= 10*

    LLIL_RBIT *= 147*

    LLIL_REG *= 12*

    LLIL_REG_PHI *= 139*

    LLIL_REG_SPLIT *= 13*

    LLIL_REG_SPLIT_DEST_SSA *= 112*

    LLIL_REG_SPLIT_SSA *= 116*

    LLIL_REG_SSA *= 114*

    LLIL_REG_SSA_PARTIAL *= 115*

    LLIL_REG_STACK_ABS_SSA *= 118*

    LLIL_REG_STACK_DEST_SSA *= 113*

    LLIL_REG_STACK_FREE_ABS_SSA *= 120*

    LLIL_REG_STACK_FREE_REG *= 16*

    LLIL_REG_STACK_FREE_REL *= 17*

    LLIL_REG_STACK_FREE_REL_SSA *= 119*

    LLIL_REG_STACK_PHI *= 140*

    LLIL_REG_STACK_POP *= 15*

    LLIL_REG_STACK_PUSH *= 5*

    LLIL_REG_STACK_REL *= 14*

    LLIL_REG_STACK_REL_SSA *= 117*

    LLIL_RET *= 59*

    LLIL_RLC *= 35*

    LLIL_ROL *= 34*

    LLIL_ROR *= 36*

    LLIL_ROUND_TO_INT *= 95*

    LLIL_RRC *= 37*

    LLIL_SBB *= 27*

    LLIL_SEPARATE_PARAM_LIST_SSA *= 132*

    LLIL_SET_FLAG *= 3*

    LLIL_SET_FLAG_SSA *= 121*

    LLIL_SET_REG *= 1*

    LLIL_SET_REG_SPLIT *= 2*

    LLIL_SET_REG_SPLIT_SSA *= 109*

    LLIL_SET_REG_SSA *= 107*

    LLIL_SET_REG_SSA_PARTIAL *= 108*

    LLIL_SET_REG_STACK_ABS_SSA *= 111*

    LLIL_SET_REG_STACK_REL *= 4*

    LLIL_SET_REG_STACK_REL_SSA *= 110*

    LLIL_SHARED_PARAM_SLOT_SSA *= 133*

    LLIL_STORE *= 9*

    LLIL_STORE_SSA *= 136*

    LLIL_SUB *= 26*

    LLIL_SX *= 51*

    LLIL_SYSCALL *= 78*

    LLIL_SYSCALL_SSA *= 127*

    LLIL_TAILCALL *= 58*

    LLIL_TAILCALL_SSA *= 128*

    LLIL_TEST_BIT *= 75*

    LLIL_TRAP *= 80*

    LLIL_UNDEF *= 82*

    LLIL_UNIMPL *= 83*

    LLIL_UNIMPL_MEM *= 84*

    LLIL_XOR *= 30*

    LLIL_ZX *= 52*

## MediumLevelILOperation

*class* MediumLevelILOperation[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MediumLevelILOperation)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    MLIL_ABS *= 159*

    MLIL_ADC *= 24*

    MLIL_ADD *= 23*

    MLIL_ADDRESS_OF *= 13*

    MLIL_ADDRESS_OF_FIELD *= 14*

    MLIL_ADD_OVERFLOW *= 80*

    MLIL_AND *= 27*

    MLIL_ASR *= 32*

    MLIL_ASSERT *= 4*

    MLIL_ASSERT_SSA *= 124*

    MLIL_BLOCK_TO_EXPAND *= 148*

    MLIL_BOOL_TO_INT *= 79*

    MLIL_BP *= 87*

    MLIL_BSWAP *= 149*

    MLIL_CALL *= 56*

    MLIL_CALL_OUTPUT_SSA *= 133*

    MLIL_CALL_PARAM *= 58*

    MLIL_CALL_PARAM_SSA *= 132*

    MLIL_CALL_SSA *= 126*

    MLIL_CALL_UNTYPED *= 57*

    MLIL_CALL_UNTYPED_SSA *= 127*

    MLIL_CEIL *= 104*

    MLIL_CLS *= 154*

    MLIL_CLZ *= 151*

    MLIL_CMP_E *= 68*

    MLIL_CMP_NE *= 69*

    MLIL_CMP_SGE *= 74*

    MLIL_CMP_SGT *= 76*

    MLIL_CMP_SLE *= 72*

    MLIL_CMP_SLT *= 70*

    MLIL_CMP_UGE *= 75*

    MLIL_CMP_UGT *= 77*

    MLIL_CMP_ULE *= 73*

    MLIL_CMP_ULT *= 71*

    MLIL_CONST *= 17*

    MLIL_CONST_DATA *= 18*

    MLIL_CONST_PTR *= 19*

    MLIL_CTZ *= 152*

    MLIL_DIVS *= 42*

    MLIL_DIVS_DP *= 43*

    MLIL_DIVU *= 40*

    MLIL_DIVU_DP *= 41*

    MLIL_EXTERN_PTR *= 20*

    MLIL_FABS *= 98*

    MLIL_FADD *= 92*

    MLIL_FCMP_E *= 106*

    MLIL_FCMP_GE *= 110*

    MLIL_FCMP_GT *= 111*

    MLIL_FCMP_LE *= 109*

    MLIL_FCMP_LT *= 108*

    MLIL_FCMP_NE *= 107*

    MLIL_FCMP_O *= 112*

    MLIL_FCMP_UO *= 113*

    MLIL_FDIV *= 95*

    MLIL_FLOAT_CONST *= 21*

    MLIL_FLOAT_CONV *= 101*

    MLIL_FLOAT_TO_INT *= 99*

    MLIL_FLOOR *= 103*

    MLIL_FMUL *= 94*

    MLIL_FNEG *= 97*

    MLIL_FORCE_VER *= 5*

    MLIL_FORCE_VER_SSA *= 125*

    MLIL_FREE_VAR_SLOT *= 86*

    MLIL_FREE_VAR_SLOT_SSA *= 145*

    MLIL_FSQRT *= 96*

    MLIL_FSUB *= 93*

    MLIL_FTRUNC *= 105*

    MLIL_GOTO *= 67*

    MLIL_IF *= 66*

    MLIL_IMPORT *= 22*

    MLIL_INTRINSIC *= 85*

    MLIL_INTRINSIC_SSA *= 143*

    MLIL_INT_TO_FLOAT *= 100*

    MLIL_JUMP *= 53*

    MLIL_JUMP_TO *= 54*

    MLIL_LOAD *= 6*

    MLIL_LOAD_SSA *= 139*

    MLIL_LOAD_STRUCT *= 7*

    MLIL_LOAD_STRUCT_SSA *= 140*

    MLIL_LOW_PART *= 52*

    MLIL_LSL *= 30*

    MLIL_LSR *= 31*

    MLIL_MAXS *= 156*

    MLIL_MAXU *= 158*

    MLIL_MEMORY_INTRINSIC_OUTPUT_SSA *= 138*

    MLIL_MEMORY_INTRINSIC_SSA *= 144*

    MLIL_MEM_PHI *= 147*

    MLIL_MINS *= 155*

    MLIL_MINU *= 157*

    MLIL_MODS *= 46*

    MLIL_MODS_DP *= 47*

    MLIL_MODU *= 44*

    MLIL_MODU_DP *= 45*

    MLIL_MUL *= 37*

    MLIL_MULS_DP *= 39*

    MLIL_MULU_DP *= 38*

    MLIL_NEG *= 48*

    MLIL_NOP *= 0*

    MLIL_NORET *= 65*

    MLIL_NOT *= 49*

    MLIL_OR *= 28*

    MLIL_PASS_BY_REF *= 15*

    MLIL_POPCNT *= 150*

    MLIL_RBIT *= 153*

    MLIL_RET *= 64*

    MLIL_RETURN_BY_REF *= 16*

    MLIL_RET_HINT *= 55*

    MLIL_RLC *= 34*

    MLIL_ROL *= 33*

    MLIL_ROR *= 35*

    MLIL_ROUND_TO_INT *= 102*

    MLIL_RRC *= 36*

    MLIL_SBB *= 26*

    MLIL_SEPARATE_PARAM_LIST *= 59*

    MLIL_SET_VAR *= 1*

    MLIL_SET_VAR_ALIASED *= 117*

    MLIL_SET_VAR_ALIASED_FIELD *= 118*

    MLIL_SET_VAR_FIELD *= 2*

    MLIL_SET_VAR_SPLIT *= 3*

    MLIL_SET_VAR_SPLIT_SSA *= 116*

    MLIL_SET_VAR_SSA *= 114*

    MLIL_SET_VAR_SSA_FIELD *= 115*

    MLIL_SHARED_PARAM_SLOT *= 60*

    MLIL_STORE *= 8*

    MLIL_STORE_OUTPUT *= 63*

    MLIL_STORE_SSA *= 141*

    MLIL_STORE_STRUCT *= 9*

    MLIL_STORE_STRUCT_SSA *= 142*

    MLIL_SUB *= 25*

    MLIL_SX *= 50*

    MLIL_SYSCALL *= 81*

    MLIL_SYSCALL_SSA *= 128*

    MLIL_SYSCALL_UNTYPED *= 82*

    MLIL_SYSCALL_UNTYPED_SSA *= 129*

    MLIL_TAILCALL *= 83*

    MLIL_TAILCALL_SSA *= 130*

    MLIL_TAILCALL_UNTYPED *= 84*

    MLIL_TAILCALL_UNTYPED_SSA *= 131*

    MLIL_TEST_BIT *= 78*

    MLIL_TRAP *= 88*

    MLIL_UNDEF *= 89*

    MLIL_UNIMPL *= 90*

    MLIL_UNIMPL_MEM *= 91*

    MLIL_VAR *= 10*

    MLIL_VAR_ALIASED *= 121*

    MLIL_VAR_ALIASED_FIELD *= 122*

    MLIL_VAR_FIELD *= 11*

    MLIL_VAR_OUTPUT *= 61*

    MLIL_VAR_OUTPUT_ALIASED *= 136*

    MLIL_VAR_OUTPUT_ALIASED_FIELD *= 137*

    MLIL_VAR_OUTPUT_FIELD *= 62*

    MLIL_VAR_OUTPUT_SSA *= 134*

    MLIL_VAR_OUTPUT_SSA_FIELD *= 135*

    MLIL_VAR_PHI *= 146*

    MLIL_VAR_SPLIT *= 12*

    MLIL_VAR_SPLIT_SSA *= 123*

    MLIL_VAR_SSA *= 119*

    MLIL_VAR_SSA_FIELD *= 120*

    MLIL_XOR *= 29*

    MLIL_ZX *= 51*

## MemberAccess

*class* MemberAccess[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MemberAccess)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    NoAccess *= 0*

    PrivateAccess *= 1*

    ProtectedAccess *= 2*

    PublicAccess *= 3*

## MemberScope

*class* MemberScope[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MemberScope)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    FriendScope *= 4*

    NoScope *= 0*

    StaticScope *= 1*

    ThunkScope *= 3*

    VirtualScope *= 2*

## MergeConflictDataType

*class* MergeConflictDataType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MergeConflictDataType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BinaryConflictDataType *= 2*

    JsonConflictDataType *= 1*

    TextConflictDataType *= 0*

## MessageBoxButtonResult

*class* MessageBoxButtonResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MessageBoxButtonResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CancelButton *= 3*

    NoButton *= 0*

    OKButton *= 2*

    YesButton *= 1*

## MessageBoxButtonSet

*class* MessageBoxButtonSet[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MessageBoxButtonSet)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    OKButtonSet *= 0*

    YesNoButtonSet *= 1*

    YesNoCancelButtonSet *= 2*

## MessageBoxIcon

*class* MessageBoxIcon[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MessageBoxIcon)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ErrorIcon *= 3*

    InformationIcon *= 0*

    QuestionIcon *= 1*

    WarningIcon *= 2*

## MetadataStoreFlag

*class* MetadataStoreFlag[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MetadataStoreFlag)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    __new__(*value*)

    MetadataStoreEphemeral *= 0*

    MetadataStoreMarksAnalysisChanged *= 2*

    MetadataStorePersistent *= 1*

## MetadataType

*class* MetadataType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MetadataType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ArrayDataType *= 8*

    BooleanDataType *= 1*

    DoubleDataType *= 5*

    InvalidDataType *= 0*

    KeyValueDataType *= 7*

    RawDataType *= 6*

    SignedIntegerDataType *= 4*

    StringDataType *= 2*

    UnsignedIntegerDataType *= 3*

## ModificationStatus

*class* ModificationStatus[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ModificationStatus)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    Changed *= 1*

    Inserted *= 2*

    Original *= 0*

## NameType

*class* NameType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#NameType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ConstructorNameType *= 1*

    CopyConstructorClosureNameType *= 60*

    DefaultConstructorClosureNameType *= 51*

    DestructorNameType *= 2*

    DynamicAtExitDestructorNameType *= 84*

    DynamicInitializerNameType *= 83*

    EHVectorConstructorIteratorNameType *= 57*

    EHVectorCopyConstructorIteratorNameType *= 81*

    EHVectorDestructorIteratorNameType *= 58*

    EHVectorVBaseConstructorIteratorNameType *= 59*

    EHVectorVBaseCopyConstructorIteratorNameType *= 82*

    LocalStaticGuardNameType *= 47*

    LocalStaticThreadGuardNameType *= 88*

    LocalVFTableConstructorClosureNameType *= 63*

    LocalVFTableNameType *= 62*

    ManagedVectorConstructorIteratorNameType *= 79*

    ManagedVectorCopyConstructorIteratorNameType *= 87*

    ManagedVectorDestructorIteratorNameType *= 80*

    NoNameType *= 0*

    OmniCallSigNameType *= 78*

    OperatorAndEqualNameType *= 40*

    OperatorArrayNameType *= 11*

    OperatorArrowNameType *= 12*

    OperatorArrowStarNameType *= 19*

    OperatorAssignNameType *= 5*

    OperatorBitAndNameType *= 18*

    OperatorBitOrNameType *= 30*

    OperatorCommaNameType *= 26*

    OperatorDecrementNameType *= 15*

    OperatorDeleteArrayNameType *= 65*

    OperatorDeleteNameType *= 4*

    OperatorDivideEqualNameType *= 36*

    OperatorDivideNameType *= 20*

    OperatorEqualNameType *= 9*

    OperatorGreaterThanEqualNameType *= 25*

    OperatorGreaterThanNameType *= 24*

    OperatorIncrementNameType *= 14*

    OperatorLeftShiftEqualNameType *= 39*

    OperatorLeftShiftNameType *= 7*

    OperatorLessThanEqualNameType *= 23*

    OperatorLessThanNameType *= 22*

    OperatorLogicalAndNameType *= 31*

    OperatorLogicalOrNameType *= 32*

    OperatorMinusEqualNameType *= 35*

    OperatorMinusNameType *= 16*

    OperatorModulusEqualNameType *= 37*

    OperatorModulusNameType *= 21*

    OperatorNewArrayNameType *= 64*

    OperatorNewNameType *= 3*

    OperatorNotEqualNameType *= 10*

    OperatorNotNameType *= 8*

    OperatorOrEqualNameType *= 41*

    OperatorParenthesesNameType *= 27*

    OperatorPlusEqualNameType *= 34*

    OperatorPlusNameType *= 17*

    OperatorReturnTypeNameType *= 68*

    OperatorRightShiftEqualNameType *= 38*

    OperatorRightShiftNameType *= 6*

    OperatorStarEqualNameType *= 33*

    OperatorStarNameType *= 13*

    OperatorTildeNameType *= 28*

    OperatorUnaryBitAndNameType *= 76*

    OperatorUnaryMinusNameType *= 74*

    OperatorUnaryPlusNameType *= 75*

    OperatorUnaryStarNameType *= 77*

    OperatorXorEqualNameType *= 42*

    OperatorXorNameType *= 29*

    PlacementDeleteClosureArrayNameType *= 67*

    PlacementDeleteClosureNameType *= 66*

    RttiBaseClassArray *= 71*

    RttiBaseClassDescriptor *= 70*

    RttiClassHierarchyDescriptor *= 72*

    RttiCompleteObjectLocator *= 73*

    RttiTypeDescriptor *= 69*

    ScalarDeletingDestructorNameType *= 52*

    StringNameType *= 48*

    TypeofNameType *= 46*

    UDTReturningNameType *= 61*

    UserDefinedLiteralOperatorNameType *= 89*

    VBTableNameType *= 44*

    VBaseDestructorNameType *= 49*

    VCallNameType *= 45*

    VFTableNameType *= 43*

    VectorConstructorIteratorNameType *= 53*

    VectorCopyConstructorIteratorNameType *= 85*

    VectorDeletingDestructorNameType *= 50*

    VectorDestructorIteratorNameType *= 54*

    VectorVBaseConstructorIteratorNameType *= 55*

    VectorVBaseCopyConstructorIteratorNameType *= 86*

    VirtualDisplacementMapNameType *= 56*

## NamedTypeReferenceClass

*class* NamedTypeReferenceClass[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#NamedTypeReferenceClass)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ClassNamedTypeClass *= 2*

    EnumNamedTypeClass *= 5*

    StructNamedTypeClass *= 3*

    TypedefNamedTypeClass *= 1*

    UnionNamedTypeClass *= 4*

    UnknownNamedTypeClass *= 0*

## OperatorPrecedence

*class* OperatorPrecedence[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#OperatorPrecedence)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AddOperatorPrecedence *= 11*

    AssignmentOperatorPrecedence *= 1*

    BitwiseAndOperatorPrecedence *= 7*

    BitwiseOrOperatorPrecedence *= 5*

    BitwiseXorOperatorPrecedence *= 6*

    CompareOperatorPrecedence *= 9*

    DivideOperatorPrecedence *= 14*

    EqualityOperatorPrecedence *= 8*

    HighUnaryOperatorPrecedence *= 17*

    LogicalAndOperatorPrecedence *= 4*

    LogicalOrOperatorPrecedence *= 3*

    LowUnaryOperatorPrecedence *= 15*

    MemberAndFunctionOperatorPrecedence *= 18*

    MultiplyOperatorPrecedence *= 13*

    ScopeOperatorPrecedence *= 19*

    ShiftOperatorPrecedence *= 10*

    SubOperatorPrecedence *= 12*

    TernaryOperatorPrecedence *= 2*

    TopLevelOperatorPrecedence *= 0*

    UnaryOperatorPrecedence *= 16*

## PluginCommandType

*class* PluginCommandType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginCommandType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AddressPluginCommand *= 1*

    DefaultPluginCommand *= 0*

    FunctionPluginCommand *= 3*

    GlobalPluginCommand *= 11*

    HighLevelILFunctionPluginCommand *= 8*

    HighLevelILInstructionPluginCommand *= 9*

    LowLevelILFunctionPluginCommand *= 4*

    LowLevelILInstructionPluginCommand *= 5*

    MediumLevelILFunctionPluginCommand *= 6*

    MediumLevelILInstructionPluginCommand *= 7*

    ProjectPluginCommand *= 10*

    RangePluginCommand *= 2*

## PluginDependencyConflictStatus

*class* PluginDependencyConflictStatus[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginDependencyConflictStatus)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    PluginDependencyProvenConflict *= 0*

    PluginDependencyUnknownCompatibility *= 1*

## PluginDependencyDecision

*class* PluginDependencyDecision[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginDependencyDecision)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    PluginDependencyDisable *= 1*

    PluginDependencyLoadAnyway *= 2*

    PluginDependencyReinstall *= 0*

## PluginLoadPhase

*class* PluginLoadPhase[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginLoadPhase)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    NativePluginLoadPhase *= 0*

    ScriptPluginLoadPhase *= 2*

    ScriptingProviderLoadPhase *= 1*

## PluginLoadStatus

*class* PluginLoadStatus[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginLoadStatus)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    LoadFailedStatus *= 2*

    LoadSucceededStatus *= 1*

    NotAttemptedStatus *= 0*

## PluginOrigin

*class* PluginOrigin[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginOrigin)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CommunityPluginOrigin *= 1*

    OfficialPluginOrigin *= 0*

    OtherPluginOrigin *= 2*

## PluginStatus

*class* PluginStatus[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginStatus)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    __new__(*value*)

    BeingDeletedPluginStatus *= 2048*

    BeingUpdatedPluginStatus *= 1024*

    DeletePendingPluginStatus *= 32*

    DependenciesBeingInstalledStatus *= 4096*

    DisablePendingPluginStatus *= 128*

    EnabledPluginStatus *= 2*

    InstalledPluginStatus *= 1*

    NotInstalledPluginStatus *= 0*

    PendingRestartPluginStatus *= 512*

    UpdateAvailablePluginStatus *= 16*

    UpdatePendingPluginStatus *= 64*

## PluginType

*class* PluginType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ArchitecturePluginType *= 2*

    BinaryViewPluginType *= 3*

    CorePluginType *= 0*

    HelperPluginType *= 4*

    SyncPluginType *= 5*

    UiPluginType *= 1*

## PointerBaseType

*class* PointerBaseType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PointerBaseType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AbsolutePointerBaseType *= 0*

    RelativeToBinaryStartPointerBaseType *= 2*

    RelativeToConstantPointerBaseType *= 1*

    RelativeToVariableAddressPointerBaseType *= 3*

## PointerSuffix

*class* PointerSuffix[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PointerSuffix)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    LvalueSuffix *= 4*

    Ptr64Suffix *= 0*

    ReferenceSuffix *= 3*

    RestrictSuffix *= 2*

    UnalignedSuffix *= 1*

## ReferenceType

*class* ReferenceType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ReferenceType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    NoReference *= 3*

    PointerReferenceType *= 0*

    RValueReferenceType *= 2*

    ReferenceReferenceType *= 1*

## RegisterValueType

*class* RegisterValueType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#RegisterValueType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ConstantDataAggregateValue *= 32771*

    ConstantDataSignExtendValue *= 32770*

    ConstantDataValue *= 32768*

    ConstantDataZeroExtendValue *= 32769*

    ConstantPointerValue *= 3*

    ConstantValue *= 2*

    EntryValue *= 1*

    ExternalPointerValue *= 4*

    ImportedAddressValue *= 7*

    InSetOfValues *= 13*

    LookupTableValue *= 12*

    NotInSetOfValues *= 14*

    ParameterPointerValue *= 9*

    ResultPointerValue *= 8*

    ReturnAddressValue *= 6*

    SignedRangeValue *= 10*

    StackFrameOffset *= 5*

    UndeterminedValue *= 0*

    UnsignedRangeValue *= 11*

## RelocationType

*class* RelocationType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#RelocationType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ELFCopyRelocationType *= 1*

    ELFGlobalRelocationType *= 0*

    ELFJumpSlotRelocationType *= 2*

    IgnoredRelocation *= 4*

    StandardRelocationType *= 3*

    UnhandledRelocation *= 5*

## RemoteFileType

*class* RemoteFileType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#RemoteFileType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BinaryViewAnalysisFileType *= 1*

    RawDataFileType *= 0*

    TypeArchiveFileType *= 2*

    UnknownFileType *= 3*

## RenderLayerDefaultEnableState

*class* RenderLayerDefaultEnableState[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#RenderLayerDefaultEnableState)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AlwaysEnabledRenderLayerDefaultEnableState *= 2*

    DisabledByDefaultRenderLayerDefaultEnableState *= 0*

    EnabledByDefaultRenderLayerDefaultEnableState *= 1*

## ReportType

*class* ReportType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ReportType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    FlowGraphReportType *= 3*

    HTMLReportType *= 2*

    MarkdownReportType *= 1*

    PlainTextReportType *= 0*

## SaveOption

*class* SaveOption[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SaveOption)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    __new__(*value*)

    PurgeOriginalFilenamePath *= 2*

    RemoveUndoData *= 0*

    TrimSnapshots *= 1*

## ScopeType

*class* ScopeType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ScopeType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BlockScopeType *= 2*

    CaseScopeType *= 4*

    HasSubScopeScopeType *= 1*

    OneLineScopeType *= 0*

    SwitchScopeType *= 3*

## ScriptingProviderExecuteResult

*class* ScriptingProviderExecuteResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ScriptingProviderExecuteResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    IncompleteScriptInput *= 1*

    InvalidScriptInput *= 0*

    ScriptExecutionCancelled *= 3*

    SuccessfulScriptExecution *= 2*

## ScriptingProviderInputReadyState

*class* ScriptingProviderInputReadyState[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ScriptingProviderInputReadyState)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    NotReadyForInput *= 0*

    ReadyForScriptExecution *= 1*

    ReadyForScriptProgramInput *= 2*

## SectionSemantics

*class* SectionSemantics[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SectionSemantics)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DefaultSectionSemantics *= 0*

    ExternalSectionSemantics *= 4*

    ReadOnlyCodeSectionSemantics *= 1*

    ReadOnlyDataSectionSemantics *= 2*

    ReadWriteDataSectionSemantics *= 3*

## SegmentFlag

*class* SegmentFlag[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SegmentFlag)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    __new__(*value*)

    SegmentContainsCode *= 16*

    SegmentContainsData *= 8*

    SegmentDenyExecute *= 64*

    SegmentDenyWrite *= 32*

    SegmentExecutable *= 1*

    SegmentReadable *= 4*

    SegmentWritable *= 2*

## SettingsScope

*class* SettingsScope[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SettingsScope)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    __new__(*value*)

    SettingsAutoScope *= 1*

    SettingsDefaultScope *= 2*

    SettingsInvalidScope *= 0*

    SettingsProjectScope *= 8*

    SettingsResourceScope *= 16*

    SettingsUserScope *= 4*

## SimilarityAnnotationType

*class* SimilarityAnnotationType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SimilarityAnnotationType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    SimilarityAnnotationAdded *= 0*

    SimilarityAnnotationChanged *= 2*

    SimilarityAnnotationRemoved *= 1*

## SimilarityApplyStatus

*class* SimilarityApplyStatus[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SimilarityApplyStatus)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    SimilarityApplyEntityNotFound *= 2*

    SimilarityApplyFailed *= 4*

    SimilarityApplyNodeInactive *= 1*

    SimilarityApplySuccess *= 0*

    SimilarityApplyUnsupported *= 3*

## SimilarityEntityType

*class* SimilarityEntityType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SimilarityEntityType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    SimilarityEntityFunction *= 0*

## SimilarityViewType

*class* SimilarityViewType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SimilarityViewType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    SimilarityViewFlowGraph *= 0*

    SimilarityViewLinear *= 1*

## StringType

*class* StringType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#StringType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AsciiString *= 0*

    Utf16String *= 1*

    Utf32String *= 2*

    Utf8String *= 3*

## StructureVariant

*class* StructureVariant[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#StructureVariant)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ClassStructureType *= 0*

    StructStructureType *= 1*

    UnionStructureType *= 2*

## SwitchRecovery

*class* SwitchRecovery[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SwitchRecovery)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AllowSwitchRecovery *= 2*

    DefaultSwitchRecovery *= 0*

    PreventSwitchRecovery *= 1*

## SymbolBinding

*class* SymbolBinding[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SymbolBinding)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    GlobalBinding *= 2*

    LocalBinding *= 1*

    NoBinding *= 0*

    WeakBinding *= 3*

## SymbolDisplayResult

*class* SymbolDisplayResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SymbolDisplayResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DataSymbolResult *= 1*

    NoSymbolAvailable *= 0*

    OtherSymbolResult *= 2*

## SymbolDisplayType

*class* SymbolDisplayType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SymbolDisplayType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AddressOfDataSymbols *= 1*

    DereferenceNonDataSymbols *= 2*

    DisplaySymbolOnly *= 0*

## SymbolType

*class* SymbolType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SymbolType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DataSymbol *= 3*

    ExternalSymbol *= 5*

    FunctionSymbol *= 0*

    ImportAddressSymbol *= 1*

    ImportedDataSymbol *= 4*

    ImportedFunctionSymbol *= 2*

    LibraryFunctionSymbol *= 6*

    LocalLabelSymbol *= 8*

    SymbolicFunctionSymbol *= 7*

## SyncStatus

*class* SyncStatus[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SyncStatus)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CanPullSyncStatus *= 4*

    CanPushAndPullSyncStatus *= 5*

    CanPushSyncStatus *= 3*

    ConflictSyncStatus *= 6*

    NoChangesSyncStatus *= 1*

    NotSyncedSyncStatus *= 0*

    UnknownSyncStatus *= 2*

## TagReferenceType

*class* TagReferenceType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TagReferenceType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AddressTagReference *= 0*

    DataTagReference *= 2*

    FunctionTagReference *= 1*

## TagTypeType

*class* TagTypeType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TagTypeType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BookmarksTagType *= 2*

    NotificationTagType *= 1*

    UserTagType *= 0*

## ThemeColor

*class* ThemeColor[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ThemeColor)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ActivePaneBackgroundColor *= 96*

    AddressColor *= 0*

    AlphanumericHighlightColor *= 10*

    AltFalseBranchColor *= 25*

    AltTrueBranchColor *= 24*

    AltUnconditionalBranchColor *= 26*

    AnnotationColor *= 40*

    ArrayTypeColor *= 122*

    BackgroundHighlightDarkColor *= 6*

    BackgroundHighlightLightColor *= 7*

    BaseStructureNameColor *= 57*

    BlackStandardHighlightColor *= 72*

    BlueStandardHighlightColor *= 64*

    BoldBackgroundHighlightDarkColor *= 8*

    BoldBackgroundHighlightLightColor *= 9*

    BoolTypeColor *= 118*

    BraceOption1Color *= 108*

    BraceOption2Color *= 109*

    BraceOption3Color *= 110*

    BraceOption4Color *= 111*

    BraceOption5Color *= 112*

    BraceOption6Color *= 113*

    CodeSymbolColor *= 30*

    CommentColor *= 55*

    CyanStandardHighlightColor *= 66*

    DataSymbolColor *= 31*

    EnumerationTypeColor *= 116*

    ExportColor *= 35*

    FalseBranchColor *= 22*

    FeatureMapAsciiStringColor *= 78*

    FeatureMapBaseColor *= 74*

    FeatureMapDataVariableColor *= 77*

    FeatureMapExternColor *= 82*

    FeatureMapFunctionColor *= 80*

    FeatureMapImportColor *= 81*

    FeatureMapLibraryColor *= 83*

    FeatureMapNavHighlightColor *= 76*

    FeatureMapNavLineColor *= 75*

    FeatureMapUnicodeStringColor *= 79*

    FieldNameColor *= 49*

    FloatTypeColor *= 120*

    FocusedPaneBackgroundColor *= 98*

    FunctionTypeColor *= 117*

    GotoLabelColor *= 54*

    GraphBackgroundDarkColor *= 12*

    GraphBackgroundLightColor *= 13*

    GraphEntryNodeIndicatorColor *= 18*

    GraphExitNodeIndicatorColor *= 19*

    GraphExitNoreturnNodeIndicatorColor *= 20*

    GraphNodeDarkColor *= 14*

    GraphNodeLightColor *= 15*

    GraphNodeOutlineColor *= 16*

    GraphNodeShadowColor *= 17*

    GreenStandardHighlightColor *= 65*

    ImportColor *= 34*

    InactivePaneBackgroundColor *= 97*

    IndentationLineColor *= 58*

    IndentationLineHighlightColor *= 59*

    InsertedColor *= 2*

    InstructionColor *= 27*

    InstructionHighlightColor *= 36*

    IntegerTypeColor *= 119*

    KeywordColor *= 50*

    LinearDisassemblyBlockColor *= 43*

    LinearDisassemblyCodeFoldColor *= 46*

    LinearDisassemblyFunctionHeaderColor *= 42*

    LinearDisassemblyNoteColor *= 44*

    LinearDisassemblySeparatorColor *= 45*

    LocalVariableColor *= 32*

    MagentaStandardHighlightColor *= 68*

    MiniGraphOverlayColor *= 73*

    ModifiedColor *= 1*

    NameSpaceColor *= 52*

    NameSpaceSeparatorColor *= 53*

    NamedTypeReferenceColor *= 125*

    NotPresentColor *= 3*

    NumberColor *= 29*

    OpcodeColor *= 41*

    OperationColor *= 56*

    OrangeStandardHighlightColor *= 70*

    OutlineColor *= 5*

    PointerTypeColor *= 121*

    PrintableHighlightColor *= 11*

    RedStandardHighlightColor *= 67*

    RegisterColor *= 28*

    RelatedInstructionHighlightColor *= 37*

    ScriptConsoleEchoColor *= 63*

    ScriptConsoleErrorColor *= 62*

    ScriptConsoleOutputColor *= 60*

    ScriptConsoleWarningColor *= 61*

    SelectionColor *= 4*

    SidebarActiveBackgroundColor *= 90*

    SidebarActiveIconColor *= 87*

    SidebarActiveIndicatorLineColor *= 92*

    SidebarBackgroundColor *= 84*

    SidebarFocusedBackgroundColor *= 91*

    SidebarFocusedIconColor *= 88*

    SidebarHeaderBackgroundColor *= 93*

    SidebarHeaderTextColor *= 94*

    SidebarHoverBackgroundColor *= 89*

    SidebarHoverIconColor *= 86*

    SidebarInactiveIconColor *= 85*

    SidebarWidgetBackgroundColor *= 95*

    StackVariableColor *= 33*

    StatusBarProjectColor *= 107*

    StatusBarServerConnectedColor *= 104*

    StatusBarServerDisconnectedColor *= 105*

    StatusBarServerWarningColor *= 106*

    StringColor *= 47*

    StructureTypeColor *= 115*

    TabBarTabActiveColor *= 99*

    TabBarTabBorderColor *= 102*

    TabBarTabGlowColor *= 103*

    TabBarTabHoverColor *= 100*

    TabBarTabInactiveColor *= 101*

    TokenHighlightColor *= 38*

    TokenSelectionColor *= 39*

    TrueBranchColor *= 21*

    TypeNameColor *= 48*

    UncertainColor *= 51*

    UnconditionalBranchColor *= 23*

    ValueTypeColor *= 124*

    VarArgsTypeColor *= 123*

    VoidTypeColor *= 114*

    WhiteStandardHighlightColor *= 71*

    WideCharTypeColor *= 126*

    YellowStandardHighlightColor *= 69*

## TokenEscapingType

*class* TokenEscapingType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TokenEscapingType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BackticksTokenEscapingType *= 1*

    NoTokenEscapingType *= 0*

    QuotedStringEscapingType *= 2*

    ReplaceInvalidCharsEscapingType *= 3*

## TransformCapabilities

*class* TransformCapabilities[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TransformCapabilities)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    __new__(*value*)

    TransformNoCapabilities *= 0*

    TransformSupportsContext *= 2*

    TransformSupportsDetection *= 1*

## TransformResult

*class* TransformResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TransformResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    TransformFailure *= 2*

    TransformNotAttempted *= 1*

    TransformRequiresPassword *= 3*

    TransformSuccess *= 0*

## TransformSessionMode

*class* TransformSessionMode[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TransformSessionMode)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    TransformSessionModeDisabled *= 0*

    TransformSessionModeFull *= 1*

    TransformSessionModeInteractive *= 2*

## TransformType

*class* TransformType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TransformType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BinaryCodecTransform *= 0*

    BinaryEncodeTransform *= 4*

    DecodeTransform *= 3*

    EncryptTransform *= 6*

    HashTransform *= 8*

    InvertingTransform *= 7*

    TextCodecTransform *= 1*

    TextEncodeTransform *= 5*

    UnicodeCodecTransform *= 2*

## TypeClass

*class* TypeClass[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TypeClass)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ArrayTypeClass *= 7*

    BoolTypeClass *= 1*

    EnumerationTypeClass *= 5*

    FloatTypeClass *= 3*

    FragmentTypeClass *= 13*

    FunctionTypeClass *= 8*

    IntegerTypeClass *= 2*

    NamedTypeReferenceClass *= 11*

    PointerTypeClass *= 6*

    StructureTypeClass *= 4*

    ValueTypeClass *= 10*

    VarArgsTypeClass *= 9*

    VoidTypeClass *= 0*

    WideCharTypeClass *= 12*

## TypeContainerType

*class* TypeContainerType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TypeContainerType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AnalysisAutoTypeContainerType *= 1*

    AnalysisTypeContainerType *= 0*

    AnalysisUserTypeContainerType *= 2*

    DebugInfoTypeContainerType *= 5*

    EmptyTypeContainerType *= 7*

    OtherTypeContainerType *= 8*

    PlatformTypeContainerType *= 6*

    TypeArchiveTypeContainerType *= 4*

    TypeLibraryTypeContainerType *= 3*

## TypeDefinitionLineType

*class* TypeDefinitionLineType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TypeDefinitionLineType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CollapsedPaddingLineType *= 9*

    EmptyLineType *= 10*

    EnumDefinitionEndLineType *= 6*

    EnumDefinitionLineType *= 4*

    EnumMemberLineType *= 5*

    PaddingLineType *= 7*

    StructDefinitionEndLineType *= 3*

    StructDefinitionLineType *= 1*

    StructFieldLineType *= 2*

    TypedefLineType *= 0*

    UndefinedXrefLineType *= 8*

## TypeParserErrorSeverity

*class* TypeParserErrorSeverity[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TypeParserErrorSeverity)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    ErrorSeverity *= 4*

    FatalSeverity *= 5*

    IgnoredSeverity *= 0*

    NoteSeverity *= 1*

    RemarkSeverity *= 2*

    WarningSeverity *= 3*

## TypeParserOption

*class* TypeParserOption[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TypeParserOption)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    BuiltinMacros *= 1*

    IncludeSystemTypes *= 0*

## TypeReferenceType

*class* TypeReferenceType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TypeReferenceType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    DirectTypeReferenceType *= 0*

    IndirectTypeReferenceType *= 1*

    UnknownTypeReferenceType *= 2*

## UpdateResult

*class* UpdateResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#UpdateResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    AlreadyUpToDate *= 2*

    UpdateAvailable *= 3*

    UpdateFailed *= 0*

    UpdateSuccess *= 1*

## ValueLocationSource

*class* ValueLocationSource[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ValueLocationSource)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CustomLocationSource *= 3*

    DefaultLocationSource *= 0*

    PassByReferenceLocationSource *= 2*

    PassByValueLocationSource *= 1*

## VariableSourceType

*class* VariableSourceType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#VariableSourceType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    __new__(*value*)

    CompositeParameterSourceType *= 4*

    CompositeReturnValueSourceType *= 3*

    FlagVariableSourceType *= 2*

    RegisterVariableSourceType *= 1*

    StackVariableSourceType *= 0*
