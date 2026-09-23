# enums module

| Class | Description |
| --- | --- |
| [`binaryninja.enums.ActionType`](#binaryninja.enums.ActionType "binaryninja.enums.ActionType") | An enumeration. |
| [`binaryninja.enums.AnalysisMode`](#binaryninja.enums.AnalysisMode "binaryninja.enums.AnalysisMode") | An enumeration. |
| [`binaryninja.enums.AnalysisSkipReason`](#binaryninja.enums.AnalysisSkipReason "binaryninja.enums.AnalysisSkipReason") | An enumeration. |
| [`binaryninja.enums.AnalysisState`](#binaryninja.enums.AnalysisState "binaryninja.enums.AnalysisState") | An enumeration. |
| [`binaryninja.enums.AnalysisWarningActionType`](#binaryninja.enums.AnalysisWarningActionType "binaryninja.enums.AnalysisWarningActionType") | An enumeration. |
| [`binaryninja.enums.BaseAddressDetectionConfidence`](#binaryninja.enums.BaseAddressDetectionConfidence "binaryninja.enums.BaseAddressDetectionConfidence") | An enumeration. |
| [`binaryninja.enums.BaseAddressDetectionPOISetting`](#binaryninja.enums.BaseAddressDetectionPOISetting "binaryninja.enums.BaseAddressDetectionPOISetting") | An enumeration. |
| [`binaryninja.enums.BaseAddressDetectionPOIType`](#binaryninja.enums.BaseAddressDetectionPOIType "binaryninja.enums.BaseAddressDetectionPOIType") | An enumeration. |
| [`binaryninja.enums.BinaryViewEventType`](#binaryninja.enums.BinaryViewEventType "binaryninja.enums.BinaryViewEventType") | An enumeration. |
| [`binaryninja.enums.BraceRequirement`](#binaryninja.enums.BraceRequirement "binaryninja.enums.BraceRequirement") | An enumeration. |
| [`binaryninja.enums.BranchType`](#binaryninja.enums.BranchType "binaryninja.enums.BranchType") | An enumeration. |
| [`binaryninja.enums.BuiltinType`](#binaryninja.enums.BuiltinType "binaryninja.enums.BuiltinType") | An enumeration. |
| [`binaryninja.enums.CallingConventionName`](#binaryninja.enums.CallingConventionName "binaryninja.enums.CallingConventionName") | An enumeration. |
| [`binaryninja.enums.CollaborationPermissionLevel`](#binaryninja.enums.CollaborationPermissionLevel "binaryninja.enums.CollaborationPermissionLevel") | An enumeration. |
| [`binaryninja.enums.DataFlowQueryOption`](#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption") | An enumeration. |
| [`binaryninja.enums.DeadStoreElimination`](#binaryninja.enums.DeadStoreElimination "binaryninja.enums.DeadStoreElimination") | An enumeration. |
| [`binaryninja.enums.DerivedStringLocationType`](#binaryninja.enums.DerivedStringLocationType "binaryninja.enums.DerivedStringLocationType") | An enumeration. |
| [`binaryninja.enums.DisassemblyAddressMode`](#binaryninja.enums.DisassemblyAddressMode "binaryninja.enums.DisassemblyAddressMode") | An enumeration. |
| [`binaryninja.enums.DisassemblyBlockLabels`](#binaryninja.enums.DisassemblyBlockLabels "binaryninja.enums.DisassemblyBlockLabels") | An enumeration. |
| [`binaryninja.enums.DisassemblyCallParameterHints`](#binaryninja.enums.DisassemblyCallParameterHints "binaryninja.enums.DisassemblyCallParameterHints") | An enumeration. |
| [`binaryninja.enums.DisassemblyOption`](#binaryninja.enums.DisassemblyOption "binaryninja.enums.DisassemblyOption") | An enumeration. |
| [`binaryninja.enums.EarlyReturn`](#binaryninja.enums.EarlyReturn "binaryninja.enums.EarlyReturn") | An enumeration. |
| [`binaryninja.enums.EdgePenStyle`](#binaryninja.enums.EdgePenStyle "binaryninja.enums.EdgePenStyle") | An enumeration. |
| [`binaryninja.enums.Endianness`](#binaryninja.enums.Endianness "binaryninja.enums.Endianness") | An enumeration. |
| [`binaryninja.enums.ExprFolding`](#binaryninja.enums.ExprFolding "binaryninja.enums.ExprFolding") | An enumeration. |
| [`binaryninja.enums.FindFlag`](#binaryninja.enums.FindFlag "binaryninja.enums.FindFlag") | An enumeration. |
| [`binaryninja.enums.FindRangeType`](#binaryninja.enums.FindRangeType "binaryninja.enums.FindRangeType") | An enumeration. |
| [`binaryninja.enums.FindType`](#binaryninja.enums.FindType "binaryninja.enums.FindType") | An enumeration. |
| [`binaryninja.enums.FirmwareNinjaMemoryAccessType`](#binaryninja.enums.FirmwareNinjaMemoryAccessType "binaryninja.enums.FirmwareNinjaMemoryAccessType") | An enumeration. |
| [`binaryninja.enums.FirmwareNinjaMemoryHeuristic`](#binaryninja.enums.FirmwareNinjaMemoryHeuristic "binaryninja.enums.FirmwareNinjaMemoryHeuristic") | An enumeration. |
| [`binaryninja.enums.FirmwareNinjaSectionAnalysisMode`](#binaryninja.enums.FirmwareNinjaSectionAnalysisMode "binaryninja.enums.FirmwareNinjaSectionAnalysisMode") | An enumeration. |
| [`binaryninja.enums.FirmwareNinjaSectionType`](#binaryninja.enums.FirmwareNinjaSectionType "binaryninja.enums.FirmwareNinjaSectionType") | An enumeration. |
| [`binaryninja.enums.FlagRole`](#binaryninja.enums.FlagRole "binaryninja.enums.FlagRole") | An enumeration. |
| [`binaryninja.enums.FlowGraphOption`](#binaryninja.enums.FlowGraphOption "binaryninja.enums.FlowGraphOption") | An enumeration. |
| [`binaryninja.enums.FormInputFieldType`](#binaryninja.enums.FormInputFieldType "binaryninja.enums.FormInputFieldType") | An enumeration. |
| [`binaryninja.enums.FunctionAnalysisSkipOverride`](#binaryninja.enums.FunctionAnalysisSkipOverride "binaryninja.enums.FunctionAnalysisSkipOverride") | An enumeration. |
| [`binaryninja.enums.FunctionGraphType`](#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType") | An enumeration. |
| [`binaryninja.enums.FunctionUpdateType`](#binaryninja.enums.FunctionUpdateType "binaryninja.enums.FunctionUpdateType") | An enumeration. |
| [`binaryninja.enums.HighLevelILOperation`](#binaryninja.enums.HighLevelILOperation "binaryninja.enums.HighLevelILOperation") | An enumeration. |
| [`binaryninja.enums.HighlightColorStyle`](#binaryninja.enums.HighlightColorStyle "binaryninja.enums.HighlightColorStyle") | An enumeration. |
| [`binaryninja.enums.HighlightStandardColor`](#binaryninja.enums.HighlightStandardColor "binaryninja.enums.HighlightStandardColor") | An enumeration. |
| [`binaryninja.enums.ILBranchDependence`](#binaryninja.enums.ILBranchDependence "binaryninja.enums.ILBranchDependence") | An enumeration. |
| [`binaryninja.enums.ILInstructionAttribute`](#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute") | An enumeration. |
| [`binaryninja.enums.ImplicitRegisterExtend`](#binaryninja.enums.ImplicitRegisterExtend "binaryninja.enums.ImplicitRegisterExtend") | An enumeration. |
| [`binaryninja.enums.InlineDuringAnalysis`](#binaryninja.enums.InlineDuringAnalysis "binaryninja.enums.InlineDuringAnalysis") | An enumeration. |
| [`binaryninja.enums.InstructionTextTokenContext`](#binaryninja.enums.InstructionTextTokenContext "binaryninja.enums.InstructionTextTokenContext") | An enumeration. |
| [`binaryninja.enums.InstructionTextTokenType`](#binaryninja.enums.InstructionTextTokenType "binaryninja.enums.InstructionTextTokenType") | An enumeration. |
| [`binaryninja.enums.IntegerDisplayType`](#binaryninja.enums.IntegerDisplayType "binaryninja.enums.IntegerDisplayType") | An enumeration. |
| [`binaryninja.enums.IntrinsicClass`](#binaryninja.enums.IntrinsicClass "binaryninja.enums.IntrinsicClass") | An enumeration. |
| [`binaryninja.enums.LinearDisassemblyLineType`](#binaryninja.enums.LinearDisassemblyLineType "binaryninja.enums.LinearDisassemblyLineType") | An enumeration. |
| [`binaryninja.enums.LinearViewObjectIdentifierType`](#binaryninja.enums.LinearViewObjectIdentifierType "binaryninja.enums.LinearViewObjectIdentifierType") | An enumeration. |
| [`binaryninja.enums.LogLevel`](#binaryninja.enums.LogLevel "binaryninja.enums.LogLevel") | An enumeration. |
| [`binaryninja.enums.LowLevelILFlagCondition`](#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | An enumeration. |
| [`binaryninja.enums.LowLevelILOperation`](#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation") | An enumeration. |
| [`binaryninja.enums.MediumLevelILOperation`](#binaryninja.enums.MediumLevelILOperation "binaryninja.enums.MediumLevelILOperation") | An enumeration. |
| [`binaryninja.enums.MemberAccess`](#binaryninja.enums.MemberAccess "binaryninja.enums.MemberAccess") | An enumeration. |
| [`binaryninja.enums.MemberScope`](#binaryninja.enums.MemberScope "binaryninja.enums.MemberScope") | An enumeration. |
| [`binaryninja.enums.MergeConflictDataType`](#binaryninja.enums.MergeConflictDataType "binaryninja.enums.MergeConflictDataType") | An enumeration. |
| [`binaryninja.enums.MessageBoxButtonResult`](#binaryninja.enums.MessageBoxButtonResult "binaryninja.enums.MessageBoxButtonResult") | An enumeration. |
| [`binaryninja.enums.MessageBoxButtonSet`](#binaryninja.enums.MessageBoxButtonSet "binaryninja.enums.MessageBoxButtonSet") | An enumeration. |
| [`binaryninja.enums.MessageBoxIcon`](#binaryninja.enums.MessageBoxIcon "binaryninja.enums.MessageBoxIcon") | An enumeration. |
| [`binaryninja.enums.MetadataType`](#binaryninja.enums.MetadataType "binaryninja.enums.MetadataType") | An enumeration. |
| [`binaryninja.enums.ModificationStatus`](#binaryninja.enums.ModificationStatus "binaryninja.enums.ModificationStatus") | An enumeration. |
| [`binaryninja.enums.NameType`](#binaryninja.enums.NameType "binaryninja.enums.NameType") | An enumeration. |
| [`binaryninja.enums.NamedTypeReferenceClass`](#binaryninja.enums.NamedTypeReferenceClass "binaryninja.enums.NamedTypeReferenceClass") | An enumeration. |
| [`binaryninja.enums.OperatorPrecedence`](#binaryninja.enums.OperatorPrecedence "binaryninja.enums.OperatorPrecedence") | An enumeration. |
| [`binaryninja.enums.PluginCommandType`](#binaryninja.enums.PluginCommandType "binaryninja.enums.PluginCommandType") | An enumeration. |
| [`binaryninja.enums.PluginLoadOrder`](#binaryninja.enums.PluginLoadOrder "binaryninja.enums.PluginLoadOrder") | An enumeration. |
| [`binaryninja.enums.PluginLoadStatus`](#binaryninja.enums.PluginLoadStatus "binaryninja.enums.PluginLoadStatus") | An enumeration. |
| [`binaryninja.enums.PluginOrigin`](#binaryninja.enums.PluginOrigin "binaryninja.enums.PluginOrigin") | An enumeration. |
| [`binaryninja.enums.PluginStatus`](#binaryninja.enums.PluginStatus "binaryninja.enums.PluginStatus") | An enumeration. |
| [`binaryninja.enums.PluginType`](#binaryninja.enums.PluginType "binaryninja.enums.PluginType") | An enumeration. |
| [`binaryninja.enums.PointerBaseType`](#binaryninja.enums.PointerBaseType "binaryninja.enums.PointerBaseType") | An enumeration. |
| [`binaryninja.enums.PointerSuffix`](#binaryninja.enums.PointerSuffix "binaryninja.enums.PointerSuffix") | An enumeration. |
| [`binaryninja.enums.ReferenceType`](#binaryninja.enums.ReferenceType "binaryninja.enums.ReferenceType") | An enumeration. |
| [`binaryninja.enums.RegisterValueType`](#binaryninja.enums.RegisterValueType "binaryninja.enums.RegisterValueType") | An enumeration. |
| [`binaryninja.enums.RelocationType`](#binaryninja.enums.RelocationType "binaryninja.enums.RelocationType") | An enumeration. |
| [`binaryninja.enums.RemoteFileType`](#binaryninja.enums.RemoteFileType "binaryninja.enums.RemoteFileType") | An enumeration. |
| [`binaryninja.enums.RenderLayerDefaultEnableState`](#binaryninja.enums.RenderLayerDefaultEnableState "binaryninja.enums.RenderLayerDefaultEnableState") | An enumeration. |
| [`binaryninja.enums.ReportType`](#binaryninja.enums.ReportType "binaryninja.enums.ReportType") | An enumeration. |
| [`binaryninja.enums.SaveOption`](#binaryninja.enums.SaveOption "binaryninja.enums.SaveOption") | An enumeration. |
| [`binaryninja.enums.ScopeType`](#binaryninja.enums.ScopeType "binaryninja.enums.ScopeType") | An enumeration. |
| [`binaryninja.enums.ScriptingProviderExecuteResult`](#binaryninja.enums.ScriptingProviderExecuteResult "binaryninja.enums.ScriptingProviderExecuteResult") | An enumeration. |
| [`binaryninja.enums.ScriptingProviderInputReadyState`](#binaryninja.enums.ScriptingProviderInputReadyState "binaryninja.enums.ScriptingProviderInputReadyState") | An enumeration. |
| [`binaryninja.enums.SectionSemantics`](#binaryninja.enums.SectionSemantics "binaryninja.enums.SectionSemantics") | An enumeration. |
| [`binaryninja.enums.SegmentFlag`](#binaryninja.enums.SegmentFlag "binaryninja.enums.SegmentFlag") | An enumeration. |
| [`binaryninja.enums.SettingsScope`](#binaryninja.enums.SettingsScope "binaryninja.enums.SettingsScope") | An enumeration. |
| [`binaryninja.enums.StringType`](#binaryninja.enums.StringType "binaryninja.enums.StringType") | An enumeration. |
| [`binaryninja.enums.StructureVariant`](#binaryninja.enums.StructureVariant "binaryninja.enums.StructureVariant") | An enumeration. |
| [`binaryninja.enums.SwitchRecovery`](#binaryninja.enums.SwitchRecovery "binaryninja.enums.SwitchRecovery") | An enumeration. |
| [`binaryninja.enums.SymbolBinding`](#binaryninja.enums.SymbolBinding "binaryninja.enums.SymbolBinding") | An enumeration. |
| [`binaryninja.enums.SymbolDisplayResult`](#binaryninja.enums.SymbolDisplayResult "binaryninja.enums.SymbolDisplayResult") | An enumeration. |
| [`binaryninja.enums.SymbolDisplayType`](#binaryninja.enums.SymbolDisplayType "binaryninja.enums.SymbolDisplayType") | An enumeration. |
| [`binaryninja.enums.SymbolType`](#binaryninja.enums.SymbolType "binaryninja.enums.SymbolType") | An enumeration. |
| [`binaryninja.enums.SyncStatus`](#binaryninja.enums.SyncStatus "binaryninja.enums.SyncStatus") | An enumeration. |
| [`binaryninja.enums.TagReferenceType`](#binaryninja.enums.TagReferenceType "binaryninja.enums.TagReferenceType") | An enumeration. |
| [`binaryninja.enums.TagTypeType`](#binaryninja.enums.TagTypeType "binaryninja.enums.TagTypeType") | An enumeration. |
| [`binaryninja.enums.ThemeColor`](#binaryninja.enums.ThemeColor "binaryninja.enums.ThemeColor") | An enumeration. |
| [`binaryninja.enums.TokenEscapingType`](#binaryninja.enums.TokenEscapingType "binaryninja.enums.TokenEscapingType") | An enumeration. |
| [`binaryninja.enums.TransformCapabilities`](#binaryninja.enums.TransformCapabilities "binaryninja.enums.TransformCapabilities") | An enumeration. |
| [`binaryninja.enums.TransformResult`](#binaryninja.enums.TransformResult "binaryninja.enums.TransformResult") | An enumeration. |
| [`binaryninja.enums.TransformSessionMode`](#binaryninja.enums.TransformSessionMode "binaryninja.enums.TransformSessionMode") | An enumeration. |
| [`binaryninja.enums.TransformType`](#binaryninja.enums.TransformType "binaryninja.enums.TransformType") | An enumeration. |
| [`binaryninja.enums.TypeClass`](#binaryninja.enums.TypeClass "binaryninja.enums.TypeClass") | An enumeration. |
| [`binaryninja.enums.TypeContainerType`](#binaryninja.enums.TypeContainerType "binaryninja.enums.TypeContainerType") | An enumeration. |
| [`binaryninja.enums.TypeDefinitionLineType`](#binaryninja.enums.TypeDefinitionLineType "binaryninja.enums.TypeDefinitionLineType") | An enumeration. |
| [`binaryninja.enums.TypeParserErrorSeverity`](#binaryninja.enums.TypeParserErrorSeverity "binaryninja.enums.TypeParserErrorSeverity") | An enumeration. |
| [`binaryninja.enums.TypeParserOption`](#binaryninja.enums.TypeParserOption "binaryninja.enums.TypeParserOption") | An enumeration. |
| [`binaryninja.enums.TypeReferenceType`](#binaryninja.enums.TypeReferenceType "binaryninja.enums.TypeReferenceType") | An enumeration. |
| [`binaryninja.enums.UpdateResult`](#binaryninja.enums.UpdateResult "binaryninja.enums.UpdateResult") | An enumeration. |
| [`binaryninja.enums.VariableSourceType`](#binaryninja.enums.VariableSourceType "binaryninja.enums.VariableSourceType") | An enumeration. |

## ActionType

*class* ActionType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ActionType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AnalysisAction *= 2*

    DataModificationAction *= 1*

    DataModificationAndAnalysisAction *= 3*

    TemporaryAction *= 0*

## AnalysisMode

*class* AnalysisMode[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#AnalysisMode)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    BasicAnalysisMode *= 2*

    ControlFlowAnalysisMode *= 3*

    FullAnalysisMode *= 0*

    IntermediateAnalysisMode *= 1*

## AnalysisSkipReason

*class* AnalysisSkipReason[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#AnalysisSkipReason)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

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

    An enumeration.

    DisableGuidedAnalysisWarningAction *= 3*

    ForceAnalysisWarningAction *= 1*

    NoAnalysisWarningAction *= 0*

    ShowStackGraphWarningAction *= 2*

## BaseAddressDetectionConfidence

*class* BaseAddressDetectionConfidence[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BaseAddressDetectionConfidence)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    HighConfidence *= 2*

    LowConfidence *= 1*

    NoConfidence *= 0*

## BaseAddressDetectionPOISetting

*class* BaseAddressDetectionPOISetting[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BaseAddressDetectionPOISetting)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    POIAnalysisAll *= 2*

    POIAnalysisFunctionsOnly *= 1*

    POIAnalysisStringsOnly *= 0*

## BaseAddressDetectionPOIType

*class* BaseAddressDetectionPOIType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BaseAddressDetectionPOIType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    POIDataVariable *= 2*

    POIFileEnd *= 4*

    POIFileStart *= 3*

    POIFunction *= 1*

    POIString *= 0*

## BinaryViewEventType

*class* BinaryViewEventType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BinaryViewEventType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    BinaryViewFinalizationEvent *= 0*

    BinaryViewInitialAnalysisCompletionEvent *= 1*

## BraceRequirement

*class* BraceRequirement[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BraceRequirement)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    BracesAlwaysRequired *= 2*

    BracesNotAllowed *= 1*

    OptionalBraces *= 0*

## BranchType

*class* BranchType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#BranchType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

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

    An enumeration.

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

    An enumeration.

    AdminPermission *= 1*

    EditPermission *= 2*

    ViewPermission *= 3*

## DataFlowQueryOption

*class* DataFlowQueryOption[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DataFlowQueryOption)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AllowReadingWritableMemoryQueryOption *= 1*

    FromAddressesInLookupTableQueryOption *= 0*

## DeadStoreElimination

*class* DeadStoreElimination[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DeadStoreElimination)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AllowDeadStoreElimination *= 2*

    DefaultDeadStoreElimination *= 0*

    PreventDeadStoreElimination *= 1*

## DerivedStringLocationType

*class* DerivedStringLocationType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DerivedStringLocationType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    CodeStringLocation *= 1*

    DataBackedStringLocation *= 0*

## DisassemblyAddressMode

*class* DisassemblyAddressMode[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DisassemblyAddressMode)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    AlwaysShowBlockLabels *= 1*

    NeverShowBlockLabels *= 2*

    NeverShowDefaultBlockLabels *= 0*

## DisassemblyCallParameterHints

*class* DisassemblyCallParameterHints[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DisassemblyCallParameterHints)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AlwaysShowParameterHints *= 1*

    NeverShowMatchingParameterHints *= 0*

    NeverShowParameterHints *= 2*

## DisassemblyOption

*class* DisassemblyOption[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#DisassemblyOption)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    DefaultEarlyReturn *= 0*

    FalseSideEarlyReturn *= 4*

    PreventEarlyReturn *= 1*

    SmallestSideEarlyReturn *= 2*

    TrueSideEarlyReturn *= 3*

## EdgePenStyle

*class* EdgePenStyle[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#EdgePenStyle)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    BigEndian *= 1*

    LittleEndian *= 0*

## ExprFolding

*class* ExprFolding[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ExprFolding)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AllowExprFolding *= 2*

    DefaultExprFolding *= 0*

    PreventExprFolding *= 1*

## FindFlag

*class* FindFlag[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FindFlag)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    An enumeration.

    FindCaseInsensitive *= 1*

    FindCaseSensitive *= 0*

    FindIgnoreWhitespace *= 2*

## FindRangeType

*class* FindRangeType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FindRangeType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AllRangeType *= 0*

    CurrentFunctionRangeType *= 2*

    CustomRangeType *= 1*

## FindType

*class* FindType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FindType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    FindTypeBytes *= 4*

    FindTypeConstant *= 3*

    FindTypeEscapedString *= 1*

    FindTypeRawString *= 0*

    FindTypeText *= 2*

## FirmwareNinjaMemoryAccessType

*class* FirmwareNinjaMemoryAccessType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FirmwareNinjaMemoryAccessType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    NoMemoryAccessType *= 0*

    ReadMemoryAccessType *= 1*

    WriteMemoryAccessType *= 2*

## FirmwareNinjaMemoryHeuristic

*class* FirmwareNinjaMemoryHeuristic[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FirmwareNinjaMemoryHeuristic)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    DefaultSectionAnalysisMode *= 0*

    DetectStringsSectionAnalysisMode *= 2*

    IgnorePaddingSectionAnalysisMode *= 1*

## FirmwareNinjaSectionType

*class* FirmwareNinjaSectionType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FirmwareNinjaSectionType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    CodeSectionType *= 0*

    CompressionSectionType *= 2*

    DataSectionType *= 1*

    PaddingSectionType *= 3*

## FlagRole

*class* FlagRole[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FlagRole)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    FlowGraphAllowsInlineInstructionEditing *= 4*

    FlowGraphAllowsPatching *= 3*

    FlowGraphIncludesUserComments *= 2*

    FlowGraphIsAddressable *= 6*

    FlowGraphIsWorkflowGraph *= 7*

    FlowGraphShowsSecondaryRegisterHighlighting *= 5*

    FlowGraphUsesBlockHighlights *= 0*

    FlowGraphUsesInstructionHighlights *= 1*

## FormInputFieldType

*class* FormInputFieldType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FormInputFieldType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    AlwaysSkipFunctionAnalysis *= 2*

    DefaultFunctionAnalysisSkip *= 0*

    NeverSkipFunctionAnalysis *= 1*

## FunctionGraphType

*class* FunctionGraphType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#FunctionGraphType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    FullAutoFunctionUpdate *= 1*

    IncrementalAutoFunctionUpdate *= 2*

    UserFunctionUpdate *= 0*

## HighLevelILOperation

*class* HighLevelILOperation[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#HighLevelILOperation)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    HLIL_ADC *= 35*

    HLIL_ADD *= 34*

    HLIL_ADDRESS_OF *= 27*

    HLIL_ADD_OVERFLOW *= 77*

    HLIL_AND *= 38*

    HLIL_ARRAY_INDEX *= 23*

    HLIL_ARRAY_INDEX_SSA *= 118*

    HLIL_ASR *= 43*

    HLIL_ASSERT *= 20*

    HLIL_ASSERT_SSA *= 116*

    HLIL_ASSIGN *= 17*

    HLIL_ASSIGN_MEM_SSA *= 113*

    HLIL_ASSIGN_UNPACK *= 18*

    HLIL_ASSIGN_UNPACK_MEM_SSA *= 114*

    HLIL_BLOCK *= 1*

    HLIL_BOOL_TO_INT *= 76*

    HLIL_BP *= 81*

    HLIL_BREAK *= 8*

    HLIL_CALL *= 64*

    HLIL_CALL_SSA *= 121*

    HLIL_CASE *= 7*

    HLIL_CEIL *= 98*

    HLIL_CMP_E *= 65*

    HLIL_CMP_NE *= 66*

    HLIL_CMP_SGE *= 71*

    HLIL_CMP_SGT *= 73*

    HLIL_CMP_SLE *= 69*

    HLIL_CMP_SLT *= 67*

    HLIL_CMP_UGE *= 72*

    HLIL_CMP_UGT *= 74*

    HLIL_CMP_ULE *= 70*

    HLIL_CMP_ULT *= 68*

    HLIL_CONST *= 28*

    HLIL_CONST_DATA *= 29*

    HLIL_CONST_PTR *= 30*

    HLIL_CONTINUE *= 9*

    HLIL_DEREF *= 25*

    HLIL_DEREF_FIELD *= 26*

    HLIL_DEREF_FIELD_SSA *= 120*

    HLIL_DEREF_SSA *= 119*

    HLIL_DIVS *= 53*

    HLIL_DIVS_DP *= 54*

    HLIL_DIVU *= 51*

    HLIL_DIVU_DP *= 52*

    HLIL_DO_WHILE *= 4*

    HLIL_DO_WHILE_SSA *= 110*

    HLIL_EXTERN_PTR *= 31*

    HLIL_FABS *= 92*

    HLIL_FADD *= 86*

    HLIL_FCMP_E *= 100*

    HLIL_FCMP_GE *= 104*

    HLIL_FCMP_GT *= 105*

    HLIL_FCMP_LE *= 103*

    HLIL_FCMP_LT *= 102*

    HLIL_FCMP_NE *= 101*

    HLIL_FCMP_O *= 106*

    HLIL_FCMP_UO *= 107*

    HLIL_FDIV *= 89*

    HLIL_FLOAT_CONST *= 32*

    HLIL_FLOAT_CONV *= 95*

    HLIL_FLOAT_TO_INT *= 93*

    HLIL_FLOOR *= 97*

    HLIL_FMUL *= 88*

    HLIL_FNEG *= 91*

    HLIL_FOR *= 5*

    HLIL_FORCE_VER *= 19*

    HLIL_FORCE_VER_SSA *= 115*

    HLIL_FOR_SSA *= 111*

    HLIL_FSQRT *= 90*

    HLIL_FSUB *= 87*

    HLIL_FTRUNC *= 99*

    HLIL_GOTO *= 13*

    HLIL_IF *= 2*

    HLIL_IMPORT *= 33*

    HLIL_INTRINSIC *= 80*

    HLIL_INTRINSIC_SSA *= 123*

    HLIL_INT_TO_FLOAT *= 94*

    HLIL_JUMP *= 10*

    HLIL_LABEL *= 14*

    HLIL_LOW_PART *= 63*

    HLIL_LSL *= 41*

    HLIL_LSR *= 42*

    HLIL_MEM_PHI *= 125*

    HLIL_MODS *= 57*

    HLIL_MODS_DP *= 58*

    HLIL_MODU *= 55*

    HLIL_MODU_DP *= 56*

    HLIL_MUL *= 48*

    HLIL_MULS_DP *= 50*

    HLIL_MULU_DP *= 49*

    HLIL_NEG *= 59*

    HLIL_NOP *= 0*

    HLIL_NORET *= 12*

    HLIL_NOT *= 60*

    HLIL_OR *= 39*

    HLIL_RET *= 11*

    HLIL_RLC *= 45*

    HLIL_ROL *= 44*

    HLIL_ROR *= 46*

    HLIL_ROUND_TO_INT *= 96*

    HLIL_RRC *= 47*

    HLIL_SBB *= 37*

    HLIL_SPLIT *= 24*

    HLIL_STRUCT_FIELD *= 22*

    HLIL_SUB *= 36*

    HLIL_SWITCH *= 6*

    HLIL_SX *= 61*

    HLIL_SYSCALL *= 78*

    HLIL_SYSCALL_SSA *= 122*

    HLIL_TAILCALL *= 79*

    HLIL_TEST_BIT *= 75*

    HLIL_TRAP *= 82*

    HLIL_UNDEF *= 83*

    HLIL_UNIMPL *= 84*

    HLIL_UNIMPL_MEM *= 85*

    HLIL_UNREACHABLE *= 108*

    HLIL_VAR *= 21*

    HLIL_VAR_DECLARE *= 15*

    HLIL_VAR_INIT *= 16*

    HLIL_VAR_INIT_SSA *= 112*

    HLIL_VAR_PHI *= 124*

    HLIL_VAR_SSA *= 117*

    HLIL_WHILE *= 3*

    HLIL_WHILE_SSA *= 109*

    HLIL_XOR *= 40*

    HLIL_ZX *= 62*

## HighlightColorStyle

*class* HighlightColorStyle[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#HighlightColorStyle)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    CustomHighlightColor *= 2*

    MixedHighlightColor *= 1*

    StandardHighlightColor *= 0*

## HighlightStandardColor

*class* HighlightStandardColor[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#HighlightStandardColor)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    FalseBranchDependent *= 2*

    NotBranchDependent *= 0*

    TrueBranchDependent *= 1*

## ILInstructionAttribute

*class* ILInstructionAttribute[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ILInstructionAttribute)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    An enumeration.

    HLILEarlyReturnPossible *= 1024*

    HLILFoldableExpr *= 256*

    HLILInvertableCondition *= 512*

    HLILSwitchRecoveryPossible *= 2048*

    ILAllowDeadStoreElimination *= 1*

    ILIsCFGProtected *= 64*

    ILPreventAliasAnalysis *= 32*

    ILPreventDeadStoreElimination *= 2*

    ILTransparentCopy *= 4096*

    MLILAssumePossibleUse *= 4*

    MLILPossiblyUnusedIntermediate *= 128*

    MLILUnknownSize *= 8*

    SrcInstructionUsesPointerAuth *= 16*

## ImplicitRegisterExtend

*class* ImplicitRegisterExtend[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ImplicitRegisterExtend)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    NoExtend *= 0*

    SignExtendToFullWidth *= 2*

    ZeroExtendToFullWidth *= 1*

## InlineDuringAnalysis

*class* InlineDuringAnalysis[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#InlineDuringAnalysis)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    DoNotInlineCall *= 0*

    InlinePreservingTargetInstructionAddresses *= 1*

    InlineUsingCallAddress *= 2*

## InstructionTextTokenContext

*class* InstructionTextTokenContext[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#InstructionTextTokenContext)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

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

## IntegerDisplayType

*class* IntegerDisplayType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#IntegerDisplayType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    UnsignedDecimalDisplayType *= 5*

    UnsignedHexadecimalDisplayType *= 7*

    UnsignedOctalDisplayType *= 3*

## IntrinsicClass

*class* IntrinsicClass[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#IntrinsicClass)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    GeneralIntrinsicClass *= 0*

    MemoryIntrinsicClass *= 1*

## LinearDisassemblyLineType

*class* LinearDisassemblyLineType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LinearDisassemblyLineType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

## LinearViewObjectIdentifierType

*class* LinearViewObjectIdentifierType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LinearViewObjectIdentifierType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AddressLinearViewObject *= 1*

    AddressRangeLinearViewObject *= 2*

    SingleLinearViewObject *= 0*

## LogLevel

*class* LogLevel[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LogLevel)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AlertLog *= 4*

    DebugLog *= 0*

    ErrorLog *= 3*

    InfoLog *= 1*

    WarningLog *= 2*

## LowLevelILFlagCondition

*class* LowLevelILFlagCondition[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#LowLevelILFlagCondition)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    LLIL_ADC *= 25*

    LLIL_ADD *= 24*

    LLIL_ADD_OVERFLOW *= 77*

    LLIL_AND *= 28*

    LLIL_ASR *= 33*

    LLIL_ASSERT *= 6*

    LLIL_ASSERT_SSA *= 122*

    LLIL_BOOL_TO_INT *= 76*

    LLIL_BP *= 79*

    LLIL_CALL *= 56*

    LLIL_CALL_OUTPUT_SSA *= 131*

    LLIL_CALL_PARAM *= 129*

    LLIL_CALL_SSA *= 126*

    LLIL_CALL_STACK_ADJUST *= 57*

    LLIL_CALL_STACK_SSA *= 130*

    LLIL_CEIL *= 97*

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

    LLIL_MEMORY_INTRINSIC_OUTPUT_SSA *= 134*

    LLIL_MEMORY_INTRINSIC_SSA *= 138*

    LLIL_MEM_PHI *= 142*

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

    LLIL_PUSH *= 10*

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

    An enumeration.

    MLIL_ADC *= 22*

    MLIL_ADD *= 21*

    MLIL_ADDRESS_OF *= 13*

    MLIL_ADDRESS_OF_FIELD *= 14*

    MLIL_ADD_OVERFLOW *= 76*

    MLIL_AND *= 25*

    MLIL_ASR *= 30*

    MLIL_ASSERT *= 4*

    MLIL_ASSERT_SSA *= 120*

    MLIL_BOOL_TO_INT *= 75*

    MLIL_BP *= 83*

    MLIL_CALL *= 54*

    MLIL_CALL_OUTPUT *= 56*

    MLIL_CALL_OUTPUT_SSA *= 129*

    MLIL_CALL_PARAM *= 57*

    MLIL_CALL_PARAM_SSA *= 128*

    MLIL_CALL_SSA *= 122*

    MLIL_CALL_UNTYPED *= 55*

    MLIL_CALL_UNTYPED_SSA *= 123*

    MLIL_CEIL *= 100*

    MLIL_CMP_E *= 64*

    MLIL_CMP_NE *= 65*

    MLIL_CMP_SGE *= 70*

    MLIL_CMP_SGT *= 72*

    MLIL_CMP_SLE *= 68*

    MLIL_CMP_SLT *= 66*

    MLIL_CMP_UGE *= 71*

    MLIL_CMP_UGT *= 73*

    MLIL_CMP_ULE *= 69*

    MLIL_CMP_ULT *= 67*

    MLIL_CONST *= 15*

    MLIL_CONST_DATA *= 16*

    MLIL_CONST_PTR *= 17*

    MLIL_DIVS *= 40*

    MLIL_DIVS_DP *= 41*

    MLIL_DIVU *= 38*

    MLIL_DIVU_DP *= 39*

    MLIL_EXTERN_PTR *= 18*

    MLIL_FABS *= 94*

    MLIL_FADD *= 88*

    MLIL_FCMP_E *= 102*

    MLIL_FCMP_GE *= 106*

    MLIL_FCMP_GT *= 107*

    MLIL_FCMP_LE *= 105*

    MLIL_FCMP_LT *= 104*

    MLIL_FCMP_NE *= 103*

    MLIL_FCMP_O *= 108*

    MLIL_FCMP_UO *= 109*

    MLIL_FDIV *= 91*

    MLIL_FLOAT_CONST *= 19*

    MLIL_FLOAT_CONV *= 97*

    MLIL_FLOAT_TO_INT *= 95*

    MLIL_FLOOR *= 99*

    MLIL_FMUL *= 90*

    MLIL_FNEG *= 93*

    MLIL_FORCE_VER *= 5*

    MLIL_FORCE_VER_SSA *= 121*

    MLIL_FREE_VAR_SLOT *= 82*

    MLIL_FREE_VAR_SLOT_SSA *= 137*

    MLIL_FSQRT *= 92*

    MLIL_FSUB *= 89*

    MLIL_FTRUNC *= 101*

    MLIL_GOTO *= 63*

    MLIL_IF *= 62*

    MLIL_IMPORT *= 20*

    MLIL_INTRINSIC *= 81*

    MLIL_INTRINSIC_SSA *= 135*

    MLIL_INT_TO_FLOAT *= 96*

    MLIL_JUMP *= 51*

    MLIL_JUMP_TO *= 52*

    MLIL_LOAD *= 6*

    MLIL_LOAD_SSA *= 131*

    MLIL_LOAD_STRUCT *= 7*

    MLIL_LOAD_STRUCT_SSA *= 132*

    MLIL_LOW_PART *= 50*

    MLIL_LSL *= 28*

    MLIL_LSR *= 29*

    MLIL_MEMORY_INTRINSIC_OUTPUT_SSA *= 130*

    MLIL_MEMORY_INTRINSIC_SSA *= 136*

    MLIL_MEM_PHI *= 139*

    MLIL_MODS *= 44*

    MLIL_MODS_DP *= 45*

    MLIL_MODU *= 42*

    MLIL_MODU_DP *= 43*

    MLIL_MUL *= 35*

    MLIL_MULS_DP *= 37*

    MLIL_MULU_DP *= 36*

    MLIL_NEG *= 46*

    MLIL_NOP *= 0*

    MLIL_NORET *= 61*

    MLIL_NOT *= 47*

    MLIL_OR *= 26*

    MLIL_RET *= 60*

    MLIL_RET_HINT *= 53*

    MLIL_RLC *= 32*

    MLIL_ROL *= 31*

    MLIL_ROR *= 33*

    MLIL_ROUND_TO_INT *= 98*

    MLIL_RRC *= 34*

    MLIL_SBB *= 24*

    MLIL_SEPARATE_PARAM_LIST *= 58*

    MLIL_SET_VAR *= 1*

    MLIL_SET_VAR_ALIASED *= 113*

    MLIL_SET_VAR_ALIASED_FIELD *= 114*

    MLIL_SET_VAR_FIELD *= 2*

    MLIL_SET_VAR_SPLIT *= 3*

    MLIL_SET_VAR_SPLIT_SSA *= 112*

    MLIL_SET_VAR_SSA *= 110*

    MLIL_SET_VAR_SSA_FIELD *= 111*

    MLIL_SHARED_PARAM_SLOT *= 59*

    MLIL_STORE *= 8*

    MLIL_STORE_SSA *= 133*

    MLIL_STORE_STRUCT *= 9*

    MLIL_STORE_STRUCT_SSA *= 134*

    MLIL_SUB *= 23*

    MLIL_SX *= 48*

    MLIL_SYSCALL *= 77*

    MLIL_SYSCALL_SSA *= 124*

    MLIL_SYSCALL_UNTYPED *= 78*

    MLIL_SYSCALL_UNTYPED_SSA *= 125*

    MLIL_TAILCALL *= 79*

    MLIL_TAILCALL_SSA *= 126*

    MLIL_TAILCALL_UNTYPED *= 80*

    MLIL_TAILCALL_UNTYPED_SSA *= 127*

    MLIL_TEST_BIT *= 74*

    MLIL_TRAP *= 84*

    MLIL_UNDEF *= 85*

    MLIL_UNIMPL *= 86*

    MLIL_UNIMPL_MEM *= 87*

    MLIL_VAR *= 10*

    MLIL_VAR_ALIASED *= 117*

    MLIL_VAR_ALIASED_FIELD *= 118*

    MLIL_VAR_FIELD *= 11*

    MLIL_VAR_PHI *= 138*

    MLIL_VAR_SPLIT *= 12*

    MLIL_VAR_SPLIT_SSA *= 119*

    MLIL_VAR_SSA *= 115*

    MLIL_VAR_SSA_FIELD *= 116*

    MLIL_XOR *= 27*

    MLIL_ZX *= 49*

## MemberAccess

*class* MemberAccess[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MemberAccess)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    NoAccess *= 0*

    PrivateAccess *= 1*

    ProtectedAccess *= 2*

    PublicAccess *= 3*

## MemberScope

*class* MemberScope[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MemberScope)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    FriendScope *= 4*

    NoScope *= 0*

    StaticScope *= 1*

    ThunkScope *= 3*

    VirtualScope *= 2*

## MergeConflictDataType

*class* MergeConflictDataType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MergeConflictDataType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    BinaryConflictDataType *= 2*

    JsonConflictDataType *= 1*

    TextConflictDataType *= 0*

## MessageBoxButtonResult

*class* MessageBoxButtonResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MessageBoxButtonResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    CancelButton *= 3*

    NoButton *= 0*

    OKButton *= 2*

    YesButton *= 1*

## MessageBoxButtonSet

*class* MessageBoxButtonSet[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MessageBoxButtonSet)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    OKButtonSet *= 0*

    YesNoButtonSet *= 1*

    YesNoCancelButtonSet *= 2*

## MessageBoxIcon

*class* MessageBoxIcon[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MessageBoxIcon)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    ErrorIcon *= 3*

    InformationIcon *= 0*

    QuestionIcon *= 1*

    WarningIcon *= 2*

## MetadataType

*class* MetadataType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#MetadataType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    Changed *= 1*

    Inserted *= 2*

    Original *= 0*

## NameType

*class* NameType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#NameType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

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

    An enumeration.

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

    An enumeration.

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

## PluginLoadOrder

*class* PluginLoadOrder[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginLoadOrder)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    EarlyPluginLoadOrder *= 0*

    LatePluginLoadOrder *= 2*

    NormalPluginLoadOrder *= 1*

## PluginLoadStatus

*class* PluginLoadStatus[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginLoadStatus)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    LoadFailedStatus *= 2*

    LoadSucceededStatus *= 1*

    NotAttemptedStatus *= 0*

## PluginOrigin

*class* PluginOrigin[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginOrigin)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    CommunityPluginOrigin *= 1*

    OfficialPluginOrigin *= 0*

    OtherPluginOrigin *= 2*

## PluginStatus

*class* PluginStatus[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PluginStatus)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

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

    An enumeration.

    AbsolutePointerBaseType *= 0*

    RelativeToBinaryStartPointerBaseType *= 2*

    RelativeToConstantPointerBaseType *= 1*

    RelativeToVariableAddressPointerBaseType *= 3*

## PointerSuffix

*class* PointerSuffix[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#PointerSuffix)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    LvalueSuffix *= 4*

    Ptr64Suffix *= 0*

    ReferenceSuffix *= 3*

    RestrictSuffix *= 2*

    UnalignedSuffix *= 1*

## ReferenceType

*class* ReferenceType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ReferenceType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    NoReference *= 3*

    PointerReferenceType *= 0*

    RValueReferenceType *= 2*

    ReferenceReferenceType *= 1*

## RegisterValueType

*class* RegisterValueType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#RegisterValueType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    ConstantDataAggregateValue *= 32771*

    ConstantDataSignExtendValue *= 32770*

    ConstantDataValue *= 32768*

    ConstantDataZeroExtendValue *= 32769*

    ConstantPointerValue *= 3*

    ConstantValue *= 2*

    EntryValue *= 1*

    ExternalPointerValue *= 4*

    ImportedAddressValue *= 7*

    InSetOfValues *= 11*

    LookupTableValue *= 10*

    NotInSetOfValues *= 12*

    ReturnAddressValue *= 6*

    SignedRangeValue *= 8*

    StackFrameOffset *= 5*

    UndeterminedValue *= 0*

    UnsignedRangeValue *= 9*

## RelocationType

*class* RelocationType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#RelocationType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    BinaryViewAnalysisFileType *= 1*

    RawDataFileType *= 0*

    TypeArchiveFileType *= 2*

    UnknownFileType *= 3*

## RenderLayerDefaultEnableState

*class* RenderLayerDefaultEnableState[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#RenderLayerDefaultEnableState)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AlwaysEnabledRenderLayerDefaultEnableState *= 2*

    DisabledByDefaultRenderLayerDefaultEnableState *= 0*

    EnabledByDefaultRenderLayerDefaultEnableState *= 1*

## ReportType

*class* ReportType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ReportType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    FlowGraphReportType *= 3*

    HTMLReportType *= 2*

    MarkdownReportType *= 1*

    PlainTextReportType *= 0*

## SaveOption

*class* SaveOption[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SaveOption)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    An enumeration.

    PurgeOriginalFilenamePath *= 2*

    RemoveUndoData *= 0*

    TrimSnapshots *= 1*

## ScopeType

*class* ScopeType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ScopeType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    BlockScopeType *= 2*

    CaseScopeType *= 4*

    HasSubScopeScopeType *= 1*

    OneLineScopeType *= 0*

    SwitchScopeType *= 3*

## ScriptingProviderExecuteResult

*class* ScriptingProviderExecuteResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ScriptingProviderExecuteResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    IncompleteScriptInput *= 1*

    InvalidScriptInput *= 0*

    ScriptExecutionCancelled *= 3*

    SuccessfulScriptExecution *= 2*

## ScriptingProviderInputReadyState

*class* ScriptingProviderInputReadyState[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ScriptingProviderInputReadyState)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    NotReadyForInput *= 0*

    ReadyForScriptExecution *= 1*

    ReadyForScriptProgramInput *= 2*

## SectionSemantics

*class* SectionSemantics[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SectionSemantics)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    DefaultSectionSemantics *= 0*

    ExternalSectionSemantics *= 4*

    ReadOnlyCodeSectionSemantics *= 1*

    ReadOnlyDataSectionSemantics *= 2*

    ReadWriteDataSectionSemantics *= 3*

## SegmentFlag

*class* SegmentFlag[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SegmentFlag)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    SettingsAutoScope *= 1*

    SettingsDefaultScope *= 2*

    SettingsInvalidScope *= 0*

    SettingsProjectScope *= 8*

    SettingsResourceScope *= 16*

    SettingsUserScope *= 4*

## StringType

*class* StringType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#StringType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AsciiString *= 0*

    Utf16String *= 1*

    Utf32String *= 2*

    Utf8String *= 3*

## StructureVariant

*class* StructureVariant[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#StructureVariant)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    ClassStructureType *= 0*

    StructStructureType *= 1*

    UnionStructureType *= 2*

## SwitchRecovery

*class* SwitchRecovery[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SwitchRecovery)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AllowSwitchRecovery *= 2*

    DefaultSwitchRecovery *= 0*

    PreventSwitchRecovery *= 1*

## SymbolBinding

*class* SymbolBinding[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SymbolBinding)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    GlobalBinding *= 2*

    LocalBinding *= 1*

    NoBinding *= 0*

    WeakBinding *= 3*

## SymbolDisplayResult

*class* SymbolDisplayResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SymbolDisplayResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    DataSymbolResult *= 1*

    NoSymbolAvailable *= 0*

    OtherSymbolResult *= 2*

## SymbolDisplayType

*class* SymbolDisplayType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SymbolDisplayType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AddressOfDataSymbols *= 1*

    DereferenceNonDataSymbols *= 2*

    DisplaySymbolOnly *= 0*

## SymbolType

*class* SymbolType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#SymbolType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

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

    An enumeration.

    AddressTagReference *= 0*

    DataTagReference *= 2*

    FunctionTagReference *= 1*

## TagTypeType

*class* TagTypeType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TagTypeType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    BookmarksTagType *= 2*

    NotificationTagType *= 1*

    UserTagType *= 0*

## ThemeColor

*class* ThemeColor[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#ThemeColor)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    BackticksTokenEscapingType *= 1*

    NoTokenEscapingType *= 0*

    QuotedStringEscapingType *= 2*

    ReplaceInvalidCharsEscapingType *= 3*

## TransformCapabilities

*class* TransformCapabilities[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TransformCapabilities)
:   Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "(in Python
    v3.14)")

    An enumeration.

    TransformNoCapabilities *= 0*

    TransformSupportsContext *= 2*

    TransformSupportsDetection *= 1*

## TransformResult

*class* TransformResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TransformResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    TransformFailure *= 2*

    TransformNotAttempted *= 1*

    TransformRequiresPassword *= 3*

    TransformSuccess *= 0*

## TransformSessionMode

*class* TransformSessionMode[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TransformSessionMode)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    TransformSessionModeDisabled *= 0*

    TransformSessionModeFull *= 1*

    TransformSessionModeInteractive *= 2*

## TransformType

*class* TransformType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TransformType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

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

    An enumeration.

    ArrayTypeClass *= 7*

    BoolTypeClass *= 1*

    EnumerationTypeClass *= 5*

    FloatTypeClass *= 3*

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

    An enumeration.

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

    An enumeration.

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

    An enumeration.

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

    An enumeration.

    BuiltinMacros *= 1*

    IncludeSystemTypes *= 0*

## TypeReferenceType

*class* TypeReferenceType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#TypeReferenceType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    DirectTypeReferenceType *= 0*

    IndirectTypeReferenceType *= 1*

    UnknownTypeReferenceType *= 2*

## UpdateResult

*class* UpdateResult[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#UpdateResult)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    AlreadyUpToDate *= 2*

    UpdateAvailable *= 3*

    UpdateFailed *= 0*

    UpdateSuccess *= 1*

## VariableSourceType

*class* VariableSourceType[[source]](https://api.binary.ninja/_modules/binaryninja/enums.html#VariableSourceType)
:   Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python
    v3.14)")

    An enumeration.

    FlagVariableSourceType *= 2*

    RegisterVariableSourceType *= 1*

    StackVariableSourceType *= 0*
