# mediumlevelil module

| Class | Description |
| --- | --- |
| [`binaryninja.mediumlevelil.CoreMediumLevelILInstruction`](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction") |  |
| [`binaryninja.mediumlevelil.LLILSSAToMLILExpressionMap`](#binaryninja.mediumlevelil.LLILSSAToMLILExpressionMap "binaryninja.mediumlevelil.LLILSSAToMLILExpressionMap") |  |
| [`binaryninja.mediumlevelil.MediumLevelILAdc`](#binaryninja.mediumlevelil.MediumLevelILAdc "binaryninja.mediumlevelil.MediumLevelILAdc") |  |
| [`binaryninja.mediumlevelil.MediumLevelILAdd`](#binaryninja.mediumlevelil.MediumLevelILAdd "binaryninja.mediumlevelil.MediumLevelILAdd") |  |
| [`binaryninja.mediumlevelil.MediumLevelILAddOverflow`](#binaryninja.mediumlevelil.MediumLevelILAddOverflow "binaryninja.mediumlevelil.MediumLevelILAddOverflow") |  |
| [`binaryninja.mediumlevelil.MediumLevelILAddressOf`](#binaryninja.mediumlevelil.MediumLevelILAddressOf "binaryninja.mediumlevelil.MediumLevelILAddressOf") |  |
| [`binaryninja.mediumlevelil.MediumLevelILAddressOfField`](#binaryninja.mediumlevelil.MediumLevelILAddressOfField "binaryninja.mediumlevelil.MediumLevelILAddressOfField") |  |
| [`binaryninja.mediumlevelil.MediumLevelILAnd`](#binaryninja.mediumlevelil.MediumLevelILAnd "binaryninja.mediumlevelil.MediumLevelILAnd") |  |
| [`binaryninja.mediumlevelil.MediumLevelILAsr`](#binaryninja.mediumlevelil.MediumLevelILAsr "binaryninja.mediumlevelil.MediumLevelILAsr") |  |
| [`binaryninja.mediumlevelil.MediumLevelILAssert`](#binaryninja.mediumlevelil.MediumLevelILAssert "binaryninja.mediumlevelil.MediumLevelILAssert") |  |
| [`binaryninja.mediumlevelil.MediumLevelILAssertSsa`](#binaryninja.mediumlevelil.MediumLevelILAssertSsa "binaryninja.mediumlevelil.MediumLevelILAssertSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILBasicBlock`](#binaryninja.mediumlevelil.MediumLevelILBasicBlock "binaryninja.mediumlevelil.MediumLevelILBasicBlock") | The `MediumLevelILBasicBlock` object is returned during analysis and should not be directly… |
| [`binaryninja.mediumlevelil.MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase "binaryninja.mediumlevelil.MediumLevelILBinaryBase") |  |
| [`binaryninja.mediumlevelil.MediumLevelILBoolToInt`](#binaryninja.mediumlevelil.MediumLevelILBoolToInt "binaryninja.mediumlevelil.MediumLevelILBoolToInt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILBp`](#binaryninja.mediumlevelil.MediumLevelILBp "binaryninja.mediumlevelil.MediumLevelILBp") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCall`](#binaryninja.mediumlevelil.MediumLevelILCall "binaryninja.mediumlevelil.MediumLevelILCall") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase "binaryninja.mediumlevelil.MediumLevelILCallBase") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCallOutput`](#binaryninja.mediumlevelil.MediumLevelILCallOutput "binaryninja.mediumlevelil.MediumLevelILCallOutput") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCallOutputSsa`](#binaryninja.mediumlevelil.MediumLevelILCallOutputSsa "binaryninja.mediumlevelil.MediumLevelILCallOutputSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCallParam`](#binaryninja.mediumlevelil.MediumLevelILCallParam "binaryninja.mediumlevelil.MediumLevelILCallParam") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCallParamSsa`](#binaryninja.mediumlevelil.MediumLevelILCallParamSsa "binaryninja.mediumlevelil.MediumLevelILCallParamSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCallSsa`](#binaryninja.mediumlevelil.MediumLevelILCallSsa "binaryninja.mediumlevelil.MediumLevelILCallSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCallUntyped`](#binaryninja.mediumlevelil.MediumLevelILCallUntyped "binaryninja.mediumlevelil.MediumLevelILCallUntyped") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCallUntypedSsa`](#binaryninja.mediumlevelil.MediumLevelILCallUntypedSsa "binaryninja.mediumlevelil.MediumLevelILCallUntypedSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCarryBase`](#binaryninja.mediumlevelil.MediumLevelILCarryBase "binaryninja.mediumlevelil.MediumLevelILCarryBase") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCeil`](#binaryninja.mediumlevelil.MediumLevelILCeil "binaryninja.mediumlevelil.MediumLevelILCeil") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpE`](#binaryninja.mediumlevelil.MediumLevelILCmpE "binaryninja.mediumlevelil.MediumLevelILCmpE") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpNe`](#binaryninja.mediumlevelil.MediumLevelILCmpNe "binaryninja.mediumlevelil.MediumLevelILCmpNe") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpSge`](#binaryninja.mediumlevelil.MediumLevelILCmpSge "binaryninja.mediumlevelil.MediumLevelILCmpSge") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpSgt`](#binaryninja.mediumlevelil.MediumLevelILCmpSgt "binaryninja.mediumlevelil.MediumLevelILCmpSgt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpSle`](#binaryninja.mediumlevelil.MediumLevelILCmpSle "binaryninja.mediumlevelil.MediumLevelILCmpSle") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpSlt`](#binaryninja.mediumlevelil.MediumLevelILCmpSlt "binaryninja.mediumlevelil.MediumLevelILCmpSlt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpUge`](#binaryninja.mediumlevelil.MediumLevelILCmpUge "binaryninja.mediumlevelil.MediumLevelILCmpUge") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpUgt`](#binaryninja.mediumlevelil.MediumLevelILCmpUgt "binaryninja.mediumlevelil.MediumLevelILCmpUgt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpUle`](#binaryninja.mediumlevelil.MediumLevelILCmpUle "binaryninja.mediumlevelil.MediumLevelILCmpUle") |  |
| [`binaryninja.mediumlevelil.MediumLevelILCmpUlt`](#binaryninja.mediumlevelil.MediumLevelILCmpUlt "binaryninja.mediumlevelil.MediumLevelILCmpUlt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase "binaryninja.mediumlevelil.MediumLevelILComparisonBase") |  |
| [`binaryninja.mediumlevelil.MediumLevelILConst`](#binaryninja.mediumlevelil.MediumLevelILConst "binaryninja.mediumlevelil.MediumLevelILConst") |  |
| [`binaryninja.mediumlevelil.MediumLevelILConstBase`](#binaryninja.mediumlevelil.MediumLevelILConstBase "binaryninja.mediumlevelil.MediumLevelILConstBase") |  |
| [`binaryninja.mediumlevelil.MediumLevelILConstData`](#binaryninja.mediumlevelil.MediumLevelILConstData "binaryninja.mediumlevelil.MediumLevelILConstData") |  |
| [`binaryninja.mediumlevelil.MediumLevelILConstPtr`](#binaryninja.mediumlevelil.MediumLevelILConstPtr "binaryninja.mediumlevelil.MediumLevelILConstPtr") |  |
| [`binaryninja.mediumlevelil.MediumLevelILDivs`](#binaryninja.mediumlevelil.MediumLevelILDivs "binaryninja.mediumlevelil.MediumLevelILDivs") |  |
| [`binaryninja.mediumlevelil.MediumLevelILDivsDp`](#binaryninja.mediumlevelil.MediumLevelILDivsDp "binaryninja.mediumlevelil.MediumLevelILDivsDp") |  |
| [`binaryninja.mediumlevelil.MediumLevelILDivu`](#binaryninja.mediumlevelil.MediumLevelILDivu "binaryninja.mediumlevelil.MediumLevelILDivu") |  |
| [`binaryninja.mediumlevelil.MediumLevelILDivuDp`](#binaryninja.mediumlevelil.MediumLevelILDivuDp "binaryninja.mediumlevelil.MediumLevelILDivuDp") |  |
| [`binaryninja.mediumlevelil.MediumLevelILExpr`](#binaryninja.mediumlevelil.MediumLevelILExpr "binaryninja.mediumlevelil.MediumLevelILExpr") | `class MediumLevelILExpr` hold the index of IL Expressions. |
| [`binaryninja.mediumlevelil.MediumLevelILExternPtr`](#binaryninja.mediumlevelil.MediumLevelILExternPtr "binaryninja.mediumlevelil.MediumLevelILExternPtr") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFabs`](#binaryninja.mediumlevelil.MediumLevelILFabs "binaryninja.mediumlevelil.MediumLevelILFabs") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFadd`](#binaryninja.mediumlevelil.MediumLevelILFadd "binaryninja.mediumlevelil.MediumLevelILFadd") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFcmpE`](#binaryninja.mediumlevelil.MediumLevelILFcmpE "binaryninja.mediumlevelil.MediumLevelILFcmpE") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFcmpGe`](#binaryninja.mediumlevelil.MediumLevelILFcmpGe "binaryninja.mediumlevelil.MediumLevelILFcmpGe") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFcmpGt`](#binaryninja.mediumlevelil.MediumLevelILFcmpGt "binaryninja.mediumlevelil.MediumLevelILFcmpGt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFcmpLe`](#binaryninja.mediumlevelil.MediumLevelILFcmpLe "binaryninja.mediumlevelil.MediumLevelILFcmpLe") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFcmpLt`](#binaryninja.mediumlevelil.MediumLevelILFcmpLt "binaryninja.mediumlevelil.MediumLevelILFcmpLt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFcmpNe`](#binaryninja.mediumlevelil.MediumLevelILFcmpNe "binaryninja.mediumlevelil.MediumLevelILFcmpNe") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFcmpO`](#binaryninja.mediumlevelil.MediumLevelILFcmpO "binaryninja.mediumlevelil.MediumLevelILFcmpO") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFcmpUo`](#binaryninja.mediumlevelil.MediumLevelILFcmpUo "binaryninja.mediumlevelil.MediumLevelILFcmpUo") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFdiv`](#binaryninja.mediumlevelil.MediumLevelILFdiv "binaryninja.mediumlevelil.MediumLevelILFdiv") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFloatConst`](#binaryninja.mediumlevelil.MediumLevelILFloatConst "binaryninja.mediumlevelil.MediumLevelILFloatConst") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFloatConv`](#binaryninja.mediumlevelil.MediumLevelILFloatConv "binaryninja.mediumlevelil.MediumLevelILFloatConv") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFloatToInt`](#binaryninja.mediumlevelil.MediumLevelILFloatToInt "binaryninja.mediumlevelil.MediumLevelILFloatToInt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFloor`](#binaryninja.mediumlevelil.MediumLevelILFloor "binaryninja.mediumlevelil.MediumLevelILFloor") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFmul`](#binaryninja.mediumlevelil.MediumLevelILFmul "binaryninja.mediumlevelil.MediumLevelILFmul") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFneg`](#binaryninja.mediumlevelil.MediumLevelILFneg "binaryninja.mediumlevelil.MediumLevelILFneg") |  |
| [`binaryninja.mediumlevelil.MediumLevelILForceVer`](#binaryninja.mediumlevelil.MediumLevelILForceVer "binaryninja.mediumlevelil.MediumLevelILForceVer") |  |
| [`binaryninja.mediumlevelil.MediumLevelILForceVerSsa`](#binaryninja.mediumlevelil.MediumLevelILForceVerSsa "binaryninja.mediumlevelil.MediumLevelILForceVerSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFreeVarSlot`](#binaryninja.mediumlevelil.MediumLevelILFreeVarSlot "binaryninja.mediumlevelil.MediumLevelILFreeVarSlot") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFreeVarSlotSsa`](#binaryninja.mediumlevelil.MediumLevelILFreeVarSlotSsa "binaryninja.mediumlevelil.MediumLevelILFreeVarSlotSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFsqrt`](#binaryninja.mediumlevelil.MediumLevelILFsqrt "binaryninja.mediumlevelil.MediumLevelILFsqrt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFsub`](#binaryninja.mediumlevelil.MediumLevelILFsub "binaryninja.mediumlevelil.MediumLevelILFsub") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFtrunc`](#binaryninja.mediumlevelil.MediumLevelILFtrunc "binaryninja.mediumlevelil.MediumLevelILFtrunc") |  |
| [`binaryninja.mediumlevelil.MediumLevelILFunction`](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | `class MediumLevelILFunction` contains the list of ExpressionIndex objects that make up a… |
| [`binaryninja.mediumlevelil.MediumLevelILGoto`](#binaryninja.mediumlevelil.MediumLevelILGoto "binaryninja.mediumlevelil.MediumLevelILGoto") |  |
| [`binaryninja.mediumlevelil.MediumLevelILIf`](#binaryninja.mediumlevelil.MediumLevelILIf "binaryninja.mediumlevelil.MediumLevelILIf") |  |
| [`binaryninja.mediumlevelil.MediumLevelILImport`](#binaryninja.mediumlevelil.MediumLevelILImport "binaryninja.mediumlevelil.MediumLevelILImport") |  |
| [`binaryninja.mediumlevelil.MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | `class MediumLevelILInstruction` Medium Level Intermediate Language Instructions are infinite… |
| [`binaryninja.mediumlevelil.MediumLevelILIntToFloat`](#binaryninja.mediumlevelil.MediumLevelILIntToFloat "binaryninja.mediumlevelil.MediumLevelILIntToFloat") |  |
| [`binaryninja.mediumlevelil.MediumLevelILIntrinsic`](#binaryninja.mediumlevelil.MediumLevelILIntrinsic "binaryninja.mediumlevelil.MediumLevelILIntrinsic") |  |
| [`binaryninja.mediumlevelil.MediumLevelILIntrinsicSsa`](#binaryninja.mediumlevelil.MediumLevelILIntrinsicSsa "binaryninja.mediumlevelil.MediumLevelILIntrinsicSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILJump`](#binaryninja.mediumlevelil.MediumLevelILJump "binaryninja.mediumlevelil.MediumLevelILJump") |  |
| [`binaryninja.mediumlevelil.MediumLevelILJumpTo`](#binaryninja.mediumlevelil.MediumLevelILJumpTo "binaryninja.mediumlevelil.MediumLevelILJumpTo") |  |
| [`binaryninja.mediumlevelil.MediumLevelILLabel`](#binaryninja.mediumlevelil.MediumLevelILLabel "binaryninja.mediumlevelil.MediumLevelILLabel") |  |
| [`binaryninja.mediumlevelil.MediumLevelILLoad`](#binaryninja.mediumlevelil.MediumLevelILLoad "binaryninja.mediumlevelil.MediumLevelILLoad") |  |
| [`binaryninja.mediumlevelil.MediumLevelILLoadSsa`](#binaryninja.mediumlevelil.MediumLevelILLoadSsa "binaryninja.mediumlevelil.MediumLevelILLoadSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILLoadStruct`](#binaryninja.mediumlevelil.MediumLevelILLoadStruct "binaryninja.mediumlevelil.MediumLevelILLoadStruct") |  |
| [`binaryninja.mediumlevelil.MediumLevelILLoadStructSsa`](#binaryninja.mediumlevelil.MediumLevelILLoadStructSsa "binaryninja.mediumlevelil.MediumLevelILLoadStructSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILLowPart`](#binaryninja.mediumlevelil.MediumLevelILLowPart "binaryninja.mediumlevelil.MediumLevelILLowPart") |  |
| [`binaryninja.mediumlevelil.MediumLevelILLsl`](#binaryninja.mediumlevelil.MediumLevelILLsl "binaryninja.mediumlevelil.MediumLevelILLsl") |  |
| [`binaryninja.mediumlevelil.MediumLevelILLsr`](#binaryninja.mediumlevelil.MediumLevelILLsr "binaryninja.mediumlevelil.MediumLevelILLsr") |  |
| [`binaryninja.mediumlevelil.MediumLevelILMemPhi`](#binaryninja.mediumlevelil.MediumLevelILMemPhi "binaryninja.mediumlevelil.MediumLevelILMemPhi") |  |
| [`binaryninja.mediumlevelil.MediumLevelILMemoryIntrinsicOutputSsa`](#binaryninja.mediumlevelil.MediumLevelILMemoryIntrinsicOutputSsa "binaryninja.mediumlevelil.MediumLevelILMemoryIntrinsicOutputSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILMemoryIntrinsicSsa`](#binaryninja.mediumlevelil.MediumLevelILMemoryIntrinsicSsa "binaryninja.mediumlevelil.MediumLevelILMemoryIntrinsicSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILMods`](#binaryninja.mediumlevelil.MediumLevelILMods "binaryninja.mediumlevelil.MediumLevelILMods") |  |
| [`binaryninja.mediumlevelil.MediumLevelILModsDp`](#binaryninja.mediumlevelil.MediumLevelILModsDp "binaryninja.mediumlevelil.MediumLevelILModsDp") |  |
| [`binaryninja.mediumlevelil.MediumLevelILModu`](#binaryninja.mediumlevelil.MediumLevelILModu "binaryninja.mediumlevelil.MediumLevelILModu") |  |
| [`binaryninja.mediumlevelil.MediumLevelILModuDp`](#binaryninja.mediumlevelil.MediumLevelILModuDp "binaryninja.mediumlevelil.MediumLevelILModuDp") |  |
| [`binaryninja.mediumlevelil.MediumLevelILMul`](#binaryninja.mediumlevelil.MediumLevelILMul "binaryninja.mediumlevelil.MediumLevelILMul") |  |
| [`binaryninja.mediumlevelil.MediumLevelILMulsDp`](#binaryninja.mediumlevelil.MediumLevelILMulsDp "binaryninja.mediumlevelil.MediumLevelILMulsDp") |  |
| [`binaryninja.mediumlevelil.MediumLevelILMuluDp`](#binaryninja.mediumlevelil.MediumLevelILMuluDp "binaryninja.mediumlevelil.MediumLevelILMuluDp") |  |
| [`binaryninja.mediumlevelil.MediumLevelILNeg`](#binaryninja.mediumlevelil.MediumLevelILNeg "binaryninja.mediumlevelil.MediumLevelILNeg") |  |
| [`binaryninja.mediumlevelil.MediumLevelILNop`](#binaryninja.mediumlevelil.MediumLevelILNop "binaryninja.mediumlevelil.MediumLevelILNop") |  |
| [`binaryninja.mediumlevelil.MediumLevelILNoret`](#binaryninja.mediumlevelil.MediumLevelILNoret "binaryninja.mediumlevelil.MediumLevelILNoret") |  |
| [`binaryninja.mediumlevelil.MediumLevelILNot`](#binaryninja.mediumlevelil.MediumLevelILNot "binaryninja.mediumlevelil.MediumLevelILNot") |  |
| [`binaryninja.mediumlevelil.MediumLevelILOperationAndSize`](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") |  |
| [`binaryninja.mediumlevelil.MediumLevelILOr`](#binaryninja.mediumlevelil.MediumLevelILOr "binaryninja.mediumlevelil.MediumLevelILOr") |  |
| [`binaryninja.mediumlevelil.MediumLevelILRet`](#binaryninja.mediumlevelil.MediumLevelILRet "binaryninja.mediumlevelil.MediumLevelILRet") |  |
| [`binaryninja.mediumlevelil.MediumLevelILRetHint`](#binaryninja.mediumlevelil.MediumLevelILRetHint "binaryninja.mediumlevelil.MediumLevelILRetHint") |  |
| [`binaryninja.mediumlevelil.MediumLevelILRlc`](#binaryninja.mediumlevelil.MediumLevelILRlc "binaryninja.mediumlevelil.MediumLevelILRlc") |  |
| [`binaryninja.mediumlevelil.MediumLevelILRol`](#binaryninja.mediumlevelil.MediumLevelILRol "binaryninja.mediumlevelil.MediumLevelILRol") |  |
| [`binaryninja.mediumlevelil.MediumLevelILRor`](#binaryninja.mediumlevelil.MediumLevelILRor "binaryninja.mediumlevelil.MediumLevelILRor") |  |
| [`binaryninja.mediumlevelil.MediumLevelILRoundToInt`](#binaryninja.mediumlevelil.MediumLevelILRoundToInt "binaryninja.mediumlevelil.MediumLevelILRoundToInt") |  |
| [`binaryninja.mediumlevelil.MediumLevelILRrc`](#binaryninja.mediumlevelil.MediumLevelILRrc "binaryninja.mediumlevelil.MediumLevelILRrc") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSbb`](#binaryninja.mediumlevelil.MediumLevelILSbb "binaryninja.mediumlevelil.MediumLevelILSbb") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSeparateParamList`](#binaryninja.mediumlevelil.MediumLevelILSeparateParamList "binaryninja.mediumlevelil.MediumLevelILSeparateParamList") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSetVar`](#binaryninja.mediumlevelil.MediumLevelILSetVar "binaryninja.mediumlevelil.MediumLevelILSetVar") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSetVarAliased`](#binaryninja.mediumlevelil.MediumLevelILSetVarAliased "binaryninja.mediumlevelil.MediumLevelILSetVarAliased") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSetVarAliasedField`](#binaryninja.mediumlevelil.MediumLevelILSetVarAliasedField "binaryninja.mediumlevelil.MediumLevelILSetVarAliasedField") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSetVarField`](#binaryninja.mediumlevelil.MediumLevelILSetVarField "binaryninja.mediumlevelil.MediumLevelILSetVarField") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSetVarSplit`](#binaryninja.mediumlevelil.MediumLevelILSetVarSplit "binaryninja.mediumlevelil.MediumLevelILSetVarSplit") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSetVarSplitSsa`](#binaryninja.mediumlevelil.MediumLevelILSetVarSplitSsa "binaryninja.mediumlevelil.MediumLevelILSetVarSplitSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSetVarSsa`](#binaryninja.mediumlevelil.MediumLevelILSetVarSsa "binaryninja.mediumlevelil.MediumLevelILSetVarSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSetVarSsaField`](#binaryninja.mediumlevelil.MediumLevelILSetVarSsaField "binaryninja.mediumlevelil.MediumLevelILSetVarSsaField") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSharedParamSlot`](#binaryninja.mediumlevelil.MediumLevelILSharedParamSlot "binaryninja.mediumlevelil.MediumLevelILSharedParamSlot") |  |
| [`binaryninja.mediumlevelil.MediumLevelILStore`](#binaryninja.mediumlevelil.MediumLevelILStore "binaryninja.mediumlevelil.MediumLevelILStore") |  |
| [`binaryninja.mediumlevelil.MediumLevelILStoreSsa`](#binaryninja.mediumlevelil.MediumLevelILStoreSsa "binaryninja.mediumlevelil.MediumLevelILStoreSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILStoreStruct`](#binaryninja.mediumlevelil.MediumLevelILStoreStruct "binaryninja.mediumlevelil.MediumLevelILStoreStruct") |  |
| [`binaryninja.mediumlevelil.MediumLevelILStoreStructSsa`](#binaryninja.mediumlevelil.MediumLevelILStoreStructSsa "binaryninja.mediumlevelil.MediumLevelILStoreStructSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSub`](#binaryninja.mediumlevelil.MediumLevelILSub "binaryninja.mediumlevelil.MediumLevelILSub") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSx`](#binaryninja.mediumlevelil.MediumLevelILSx "binaryninja.mediumlevelil.MediumLevelILSx") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSyscall`](#binaryninja.mediumlevelil.MediumLevelILSyscall "binaryninja.mediumlevelil.MediumLevelILSyscall") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSyscallSsa`](#binaryninja.mediumlevelil.MediumLevelILSyscallSsa "binaryninja.mediumlevelil.MediumLevelILSyscallSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSyscallUntyped`](#binaryninja.mediumlevelil.MediumLevelILSyscallUntyped "binaryninja.mediumlevelil.MediumLevelILSyscallUntyped") |  |
| [`binaryninja.mediumlevelil.MediumLevelILSyscallUntypedSsa`](#binaryninja.mediumlevelil.MediumLevelILSyscallUntypedSsa "binaryninja.mediumlevelil.MediumLevelILSyscallUntypedSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILTailcall`](#binaryninja.mediumlevelil.MediumLevelILTailcall "binaryninja.mediumlevelil.MediumLevelILTailcall") |  |
| [`binaryninja.mediumlevelil.MediumLevelILTailcallSsa`](#binaryninja.mediumlevelil.MediumLevelILTailcallSsa "binaryninja.mediumlevelil.MediumLevelILTailcallSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILTailcallUntyped`](#binaryninja.mediumlevelil.MediumLevelILTailcallUntyped "binaryninja.mediumlevelil.MediumLevelILTailcallUntyped") |  |
| [`binaryninja.mediumlevelil.MediumLevelILTailcallUntypedSsa`](#binaryninja.mediumlevelil.MediumLevelILTailcallUntypedSsa "binaryninja.mediumlevelil.MediumLevelILTailcallUntypedSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILTestBit`](#binaryninja.mediumlevelil.MediumLevelILTestBit "binaryninja.mediumlevelil.MediumLevelILTestBit") |  |
| [`binaryninja.mediumlevelil.MediumLevelILTrap`](#binaryninja.mediumlevelil.MediumLevelILTrap "binaryninja.mediumlevelil.MediumLevelILTrap") |  |
| [`binaryninja.mediumlevelil.MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase "binaryninja.mediumlevelil.MediumLevelILUnaryBase") |  |
| [`binaryninja.mediumlevelil.MediumLevelILUndef`](#binaryninja.mediumlevelil.MediumLevelILUndef "binaryninja.mediumlevelil.MediumLevelILUndef") |  |
| [`binaryninja.mediumlevelil.MediumLevelILUnimpl`](#binaryninja.mediumlevelil.MediumLevelILUnimpl "binaryninja.mediumlevelil.MediumLevelILUnimpl") |  |
| [`binaryninja.mediumlevelil.MediumLevelILUnimplMem`](#binaryninja.mediumlevelil.MediumLevelILUnimplMem "binaryninja.mediumlevelil.MediumLevelILUnimplMem") |  |
| [`binaryninja.mediumlevelil.MediumLevelILVar`](#binaryninja.mediumlevelil.MediumLevelILVar "binaryninja.mediumlevelil.MediumLevelILVar") |  |
| [`binaryninja.mediumlevelil.MediumLevelILVarAliased`](#binaryninja.mediumlevelil.MediumLevelILVarAliased "binaryninja.mediumlevelil.MediumLevelILVarAliased") |  |
| [`binaryninja.mediumlevelil.MediumLevelILVarAliasedField`](#binaryninja.mediumlevelil.MediumLevelILVarAliasedField "binaryninja.mediumlevelil.MediumLevelILVarAliasedField") |  |
| [`binaryninja.mediumlevelil.MediumLevelILVarField`](#binaryninja.mediumlevelil.MediumLevelILVarField "binaryninja.mediumlevelil.MediumLevelILVarField") |  |
| [`binaryninja.mediumlevelil.MediumLevelILVarPhi`](#binaryninja.mediumlevelil.MediumLevelILVarPhi "binaryninja.mediumlevelil.MediumLevelILVarPhi") |  |
| [`binaryninja.mediumlevelil.MediumLevelILVarSplit`](#binaryninja.mediumlevelil.MediumLevelILVarSplit "binaryninja.mediumlevelil.MediumLevelILVarSplit") |  |
| [`binaryninja.mediumlevelil.MediumLevelILVarSplitSsa`](#binaryninja.mediumlevelil.MediumLevelILVarSplitSsa "binaryninja.mediumlevelil.MediumLevelILVarSplitSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILVarSsa`](#binaryninja.mediumlevelil.MediumLevelILVarSsa "binaryninja.mediumlevelil.MediumLevelILVarSsa") |  |
| [`binaryninja.mediumlevelil.MediumLevelILVarSsaField`](#binaryninja.mediumlevelil.MediumLevelILVarSsaField "binaryninja.mediumlevelil.MediumLevelILVarSsaField") |  |
| [`binaryninja.mediumlevelil.MediumLevelILXor`](#binaryninja.mediumlevelil.MediumLevelILXor "binaryninja.mediumlevelil.MediumLevelILXor") |  |
| [`binaryninja.mediumlevelil.MediumLevelILZx`](#binaryninja.mediumlevelil.MediumLevelILZx "binaryninja.mediumlevelil.MediumLevelILZx") |  |
| [`binaryninja.mediumlevelil.SSAVariable`](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") |  |

## CoreMediumLevelILInstruction

*class* CoreMediumLevelILInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#CoreMediumLevelILInstruction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    CoreMediumLevelILInstruction(operation: binaryninja.enums.MediumLevelILOperation,
    attributes: int, source_operand: int, size: int, operands: Tuple[ExpressionIndex,
    ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex], address: int)

    __init__(*operation: [MediumLevelILOperation](enums.md#binaryninja.enums.MediumLevelILOperation "binaryninja.enums.MediumLevelILOperation")*, *attributes: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *source_operand: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *operands: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **operation**
              ([*MediumLevelILOperation*](enums.md#binaryninja.enums.MediumLevelILOperation
              "binaryninja.enums.MediumLevelILOperation")) –
            - **attributes** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **source_operand** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **operands** ([*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[**ExpressionIndex**,* *ExpressionIndex**,* *ExpressionIndex**,*
              *ExpressionIndex**,* *ExpressionIndex**]*) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    *classmethod* from_BNMediumLevelILInstruction(*instr: BNMediumLevelILInstruction*) → [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#CoreMediumLevelILInstruction.from_BNMediumLevelILInstruction)
    :   Parameters:
        :   **instr** (*BNMediumLevelILInstruction*) –

        Return type:
        :   [*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
            "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    attributes*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    operands*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*

    operation*: [MediumLevelILOperation](enums.md#binaryninja.enums.MediumLevelILOperation "binaryninja.enums.MediumLevelILOperation")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    source_operand*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LLILSSAToMLILExpressionMap

*class* LLILSSAToMLILExpressionMap[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#LLILSSAToMLILExpressionMap)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    LLILSSAToMLILExpressionMap(lower_index: ‘lowlevelil.ExpressionIndex’, higher_index:
    <function NewType.<locals>.new_type at 0x1077f7670>, map_lower_to_higher: bool,
    map_higher_to_lower: bool, lower_to_higher_direct: bool, higher_to_lower_direct: bool)

    __init__(*lower_index: ExpressionIndex*, *higher_index: ExpressionIndex*, *map_lower_to_higher: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *map_higher_to_lower: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *lower_to_higher_direct: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *higher_to_lower_direct: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **lower_index** (*ExpressionIndex*) –
            - **higher_index** (*ExpressionIndex*) –
            - **map_lower_to_higher** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) –
            - **map_higher_to_lower** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) –
            - **lower_to_higher_direct**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) –
            - **higher_to_lower_direct**
              ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) –

        Return type:
        :   *None*

    higher_index*: ExpressionIndex*

    higher_to_lower_direct*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    lower_index*: ExpressionIndex*

    lower_to_higher_direct*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    map_higher_to_lower*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    map_lower_to_higher*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

## MediumLevelILAdc

*class* MediumLevelILAdc[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILAdc)
:   Bases: [`MediumLevelILCarryBase`](#binaryninja.mediumlevelil.MediumLevelILCarryBase
    "binaryninja.mediumlevelil.MediumLevelILCarryBase")

    MediumLevelILAdc(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILAdd

*class* MediumLevelILAdd[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILAdd)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILAdd(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILAddOverflow

*class* MediumLevelILAddOverflow[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILAddOverflow)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILAddOverflow(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILAddressOf

*class* MediumLevelILAddressOf[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILAddressOf)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILAddressOf(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    *property* vars_address_taken*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   Non-unique list of variables whose address is taken by instruction

## MediumLevelILAddressOfField

*class* MediumLevelILAddressOfField[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILAddressOfField)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILAddressOfField(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## MediumLevelILAnd

*class* MediumLevelILAnd[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILAnd)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILAnd(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILAsr

*class* MediumLevelILAsr[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILAsr)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILAsr(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILAssert

*class* MediumLevelILAssert[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILAssert)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILAssert(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* constraint*: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## MediumLevelILAssertSsa

*class* MediumLevelILAssertSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILAssertSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILAssertSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* constraint*: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## MediumLevelILBasicBlock

*class* MediumLevelILBasicBlock[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILBasicBlock)
:   Bases: [`BasicBlock`](basicblock.md#binaryninja.basicblock.BasicBlock
    "binaryninja.basicblock.BasicBlock")

    The `MediumLevelILBasicBlock` object is returned during analysis and should not be
    directly instantiated.

    __init__(*handle: LP_BNBasicBlock*, *owner: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILBasicBlock.__init__)
    :   Parameters:
        :   - **handle** (*LP_BNBasicBlock*) –
            - **owner** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*) –

    *property* il_function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*
    :   IL Function of which this block is a part, if the block is part of an IL Function.

    *property* instruction_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILBinaryBase

*class* MediumLevelILBinaryBase[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILBinaryBase)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`BinaryOperation`](commonil.md#binaryninja.commonil.BinaryOperation
    "binaryninja.commonil.BinaryOperation")

    MediumLevelILBinaryBase(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* left*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* right*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILBoolToInt

*class* MediumLevelILBoolToInt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILBoolToInt)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILBoolToInt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILBp

*class* MediumLevelILBp[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILBp)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    MediumLevelILBp(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCall

*class* MediumLevelILCall[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCall)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Localcall`](commonil.md#binaryninja.commonil.Localcall
    "binaryninja.commonil.Localcall")

    MediumLevelILCall(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

## MediumLevelILCallBase

*class* MediumLevelILCallBase[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCallBase)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Call`](commonil.md#binaryninja.commonil.Call "binaryninja.commonil.Call")

    MediumLevelILCallBase(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables written by instruction

## MediumLevelILCallOutput

*class* MediumLevelILCallOutput[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCallOutput)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILCallOutput(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables written by instruction

## MediumLevelILCallOutputSsa

*class* MediumLevelILCallOutputSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCallOutputSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILCallOutputSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables written by instruction

## MediumLevelILCallParam

*class* MediumLevelILCallParam[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCallParam)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILCallParam(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

## MediumLevelILCallParamSsa

*class* MediumLevelILCallParamSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCallParamSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILCallParamSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILCallSsa

*class* MediumLevelILCallSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCallSsa)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Localcall`](commonil.md#binaryninja.commonil.Localcall
    "binaryninja.commonil.Localcall"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    MediumLevelILCallSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* output_dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILCallUntyped

*class* MediumLevelILCallUntyped[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCallUntyped)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Localcall`](commonil.md#binaryninja.commonil.Localcall
    "binaryninja.commonil.Localcall")

    MediumLevelILCallUntyped(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* stack*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILCallUntypedSsa

*class* MediumLevelILCallUntypedSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCallUntypedSsa)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Localcall`](commonil.md#binaryninja.commonil.Localcall
    "binaryninja.commonil.Localcall"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    MediumLevelILCallUntypedSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* output_dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* params_src_memory

    *property* stack*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILCarryBase

*class* MediumLevelILCarryBase[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCarryBase)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Carry`](commonil.md#binaryninja.commonil.Carry "binaryninja.commonil.Carry")

    MediumLevelILCarryBase(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* carry*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* left*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* right*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILCeil

*class* MediumLevelILCeil[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCeil)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILCeil(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpE

*class* MediumLevelILCmpE[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpE)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase")

    MediumLevelILCmpE(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpNe

*class* MediumLevelILCmpNe[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpNe)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase")

    MediumLevelILCmpNe(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpSge

*class* MediumLevelILCmpSge[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpSge)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    MediumLevelILCmpSge(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpSgt

*class* MediumLevelILCmpSgt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpSgt)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    MediumLevelILCmpSgt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpSle

*class* MediumLevelILCmpSle[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpSle)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    MediumLevelILCmpSle(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpSlt

*class* MediumLevelILCmpSlt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpSlt)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    MediumLevelILCmpSlt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpUge

*class* MediumLevelILCmpUge[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpUge)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase")

    MediumLevelILCmpUge(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpUgt

*class* MediumLevelILCmpUgt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpUgt)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase")

    MediumLevelILCmpUgt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpUle

*class* MediumLevelILCmpUle[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpUle)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase")

    MediumLevelILCmpUle(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILCmpUlt

*class* MediumLevelILCmpUlt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILCmpUlt)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase")

    MediumLevelILCmpUlt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILComparisonBase

*class* MediumLevelILComparisonBase[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILComparisonBase)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Comparison`](commonil.md#binaryninja.commonil.Comparison
    "binaryninja.commonil.Comparison")

    MediumLevelILComparisonBase(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILConst

*class* MediumLevelILConst[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILConst)
:   Bases: [`MediumLevelILConstBase`](#binaryninja.mediumlevelil.MediumLevelILConstBase
    "binaryninja.mediumlevelil.MediumLevelILConstBase")

    MediumLevelILConst(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILConstBase

*class* MediumLevelILConstBase[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILConstBase)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Constant`](commonil.md#binaryninja.commonil.Constant "binaryninja.commonil.Constant")

    MediumLevelILConstBase(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILConstData

*class* MediumLevelILConstData[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILConstData)
:   Bases: [`MediumLevelILConstBase`](#binaryninja.mediumlevelil.MediumLevelILConstBase
    "binaryninja.mediumlevelil.MediumLevelILConstBase")

    MediumLevelILConstData(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* constant*: [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData")*

    *property* constant_data*: [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILConstPtr

*class* MediumLevelILConstPtr[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILConstPtr)
:   Bases: [`MediumLevelILConstBase`](#binaryninja.mediumlevelil.MediumLevelILConstBase
    "binaryninja.mediumlevelil.MediumLevelILConstBase")

    MediumLevelILConstPtr(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* string*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [StringType](enums.md#binaryninja.enums.StringType "binaryninja.enums.StringType")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## MediumLevelILDivs

*class* MediumLevelILDivs[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILDivs)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"), [`Signed`](commonil.md#binaryninja.commonil.Signed
    "binaryninja.commonil.Signed")

    MediumLevelILDivs(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILDivsDp

*class* MediumLevelILDivsDp[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILDivsDp)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    MediumLevelILDivsDp(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILDivu

*class* MediumLevelILDivu[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILDivu)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILDivu(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILDivuDp

*class* MediumLevelILDivuDp[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILDivuDp)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    MediumLevelILDivuDp(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILExpr

*class* MediumLevelILExpr[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILExpr)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class MediumLevelILExpr` hold the index of IL Expressions.

    Note

    Deprecated. Use ExpressionIndex instead

    __init__(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILExpr.__init__)
    :   Parameters:
        :   **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

    *property* index

## MediumLevelILExternPtr

*class* MediumLevelILExternPtr[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILExternPtr)
:   Bases: [`MediumLevelILConstBase`](#binaryninja.mediumlevelil.MediumLevelILConstBase
    "binaryninja.mediumlevelil.MediumLevelILConstBase")

    MediumLevelILExternPtr(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILFabs

*class* MediumLevelILFabs[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFabs)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFabs(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFadd

*class* MediumLevelILFadd[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFadd)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFadd(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFcmpE

*class* MediumLevelILFcmpE[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFcmpE)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFcmpE(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFcmpGe

*class* MediumLevelILFcmpGe[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFcmpGe)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFcmpGe(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFcmpGt

*class* MediumLevelILFcmpGt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFcmpGt)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFcmpGt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFcmpLe

*class* MediumLevelILFcmpLe[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFcmpLe)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFcmpLe(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFcmpLt

*class* MediumLevelILFcmpLt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFcmpLt)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFcmpLt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFcmpNe

*class* MediumLevelILFcmpNe[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFcmpNe)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFcmpNe(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFcmpO

*class* MediumLevelILFcmpO[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFcmpO)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFcmpO(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFcmpUo

*class* MediumLevelILFcmpUo[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFcmpUo)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFcmpUo(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFdiv

*class* MediumLevelILFdiv[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFdiv)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFdiv(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFloatConst

*class* MediumLevelILFloatConst[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFloatConst)
:   Bases: [`MediumLevelILConstBase`](#binaryninja.mediumlevelil.MediumLevelILConstBase
    "binaryninja.mediumlevelil.MediumLevelILConstBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFloatConst(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* constant*: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFloatConv

*class* MediumLevelILFloatConv[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFloatConv)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFloatConv(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFloatToInt

*class* MediumLevelILFloatToInt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFloatToInt)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFloatToInt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFloor

*class* MediumLevelILFloor[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFloor)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFloor(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFmul

*class* MediumLevelILFmul[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFmul)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFmul(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFneg

*class* MediumLevelILFneg[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFneg)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFneg(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILForceVer

*class* MediumLevelILForceVer[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILForceVer)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILForceVer(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## MediumLevelILForceVerSsa

*class* MediumLevelILForceVerSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILForceVerSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILForceVerSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## MediumLevelILFreeVarSlot

*class* MediumLevelILFreeVarSlot[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFreeVarSlot)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack")

    MediumLevelILFreeVarSlot(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFreeVarSlotSsa

*class* MediumLevelILFreeVarSlotSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFreeVarSlotSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack")

    MediumLevelILFreeVarSlotSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* prev*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## MediumLevelILFsqrt

*class* MediumLevelILFsqrt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFsqrt)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFsqrt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFsub

*class* MediumLevelILFsub[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFsub)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFsub(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFtrunc

*class* MediumLevelILFtrunc[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFtrunc)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILFtrunc(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILFunction

*class* MediumLevelILFunction[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class MediumLevelILFunction` contains the list of ExpressionIndex objects that make up
    a function. ExpressionIndex objects can be added to the MediumLevelILFunction by calling
    [`append`](#binaryninja.mediumlevelil.MediumLevelILFunction.append
    "binaryninja.mediumlevelil.MediumLevelILFunction.append") and passing the result of the
    various class methods which return ExpressionIndex objects.

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: BNMediumLevelILFunction | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *source_func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *low_level_il: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.__init__)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **handle** (*BNMediumLevelILFunction* *|* *None*) –
            - **source_func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –
            - **low_level_il**
              ([*LowLevelILFunction*](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction") *|* *None*) –

    add(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.add)
    :   `add` adds expression `a` to expression `b` returning an expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `add.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    add_carry(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.add_carry)
    :   `add_carry` adds expression `a` to expression `b` with carry from `carry` returning an
        expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **carry** (*ExpressionIndex*) – Carried value expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `adc.<size>(a, b, carry)`

        Return type:
        :   ExpressionIndex

    add_label_map(*labels: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [MediumLevelILLabel](#binaryninja.mediumlevelil.MediumLevelILLabel "binaryninja.mediumlevelil.MediumLevelILLabel")]*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.add_label_map)
    :   `add_label_map` returns a label list expression for the given list of MediumLevelILLabel
        objects.

        Parameters:
        :   **labels** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
            v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")*,* [*MediumLevelILLabel*](#binaryninja.mediumlevelil.MediumLevelILLabel
            "binaryninja.mediumlevelil.MediumLevelILLabel")*)*) – the list of MediumLevelILLabel to
            get a label list expression from

        Returns:
        :   the label list expression

        Return type:
        :   ExpressionIndex

    add_operand_list(*operands: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.add_operand_list)
    :   `add_operand_list` returns an operand list expression for the given list of integer
        operands.

        Parameters:
        :   **operands** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")*)*) – list of operand numbers

        Returns:
        :   an operand list expression

        Return type:
        :   ExpressionIndex

    add_variable_list(*vars: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.add_variable_list)
    :   `add_variable_list` returns a variable list expression for the given list of variables.

        Parameters:
        :   **vars** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")*(*[*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")*)*) – list of variables

        Returns:
        :   a variable list expression

        Return type:
        :   ExpressionIndex

    address_of(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.address_of)
    :   `address_of` takes the address of `var`

        Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable having its address taken
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `&var`

        Return type:
        :   ExpressionIndex

    address_of_field(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.address_of_field)
    :   `address_of_field` takes the address of `var` at the offset `offset`

        Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable having its address taken
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the offset of the taken address
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `&var:offset`

        Return type:
        :   ExpressionIndex

    and_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.and_expr)
    :   `and_expr` bitwise and’s expression `a` and expression `b` returning an expression of
        `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `and.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    append(*expr: ExpressionIndex*, *source_location: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → InstructionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.append)
    :   `append` adds the ExpressionIndex `expr` to the current MediumLevelILFunction.

        Parameters:
        :   - **expr** (*ExpressionIndex*) – the ExpressionIndex to add to the current
              MediumLevelILFunction
            - **source_location**
              ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – Optional source location for the instruction

        Returns:
        :   Index of added instruction in the current function

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    arith_shift_right(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.arith_shift_right)
    :   `arith_shift_right` arithmetically right shifts expression `a` by expression `b`
        returning an expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `asr.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    assert_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *constraint: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.assert_expr)
    :   `assert_expr` assert `constraint` is the value of the given variable `src`. Used when
        setting user variable values.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of value in the constraint
            - **src** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – variable to constrain
            - **constraint** ([*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet")) – asserted value of variable
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `ASSERT(src, constraint)`

        Return type:
        :   ExpressionIndex

    bool_to_int(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.bool_to_int)
    :   `bool_to_int` returns an expression of size `size` converting the boolean expression `a`
        to an integer

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – boolean expression to be converted
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the converted integer expression.

        Return type:
        :   ExpressionIndex

    breakpoint(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.breakpoint)
    :   `breakpoint` returns a processor breakpoint expression.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a breakpoint expression.

        Return type:
        :   ExpressionIndex

    cache_possible_value_set(*pvs: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.cache_possible_value_set)
    :   Cache a PossibleValueSet in the IL function, returning its index for use in an
        expression operand :param pvs: PossibleValueSet to cache :return: Index of the
        PossibleValueSet in the cache

        Parameters:
        :   **pvs** ([*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    call(*output: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*, *dest: ExpressionIndex*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.call)
    :   `call` returns an expression which calls the function in the expression `dest` with the
        parameters defined in `params` returning values in the variables in `output`.

        Parameters:
        :   - **output** (*List**[**'variable.Variable'**]*) – output variables
            - **dest** (*ExpressionIndex*) – the expression to call
            - **params** (*List**[**ExpressionIndex**]*) – parameter variables
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `output = call(dest, params...)`

        Return type:
        :   ExpressionIndex

    call_untyped(*output: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*, *dest: ExpressionIndex*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *stack: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.call_untyped)
    :   `call_untyped` returns an expression which calls the function in the expression `dest`
        with the parameters defined in `params` returning values in the variables in `output`
        where stack resolution could not be determined and the top of the stack has to be
        specified in `stack`

        Parameters:
        :   - **output** (*List**[**'variable.Variable'**]*) – output variables
            - **dest** (*ExpressionIndex*) – the expression to call
            - **params** (*List**[**ExpressionIndex**]*) – parameter variables
            - **stack** (*ExpressionIndex*) – expression of top of stack
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `output = call(dest, params..., stack = stack)`

        Return type:
        :   ExpressionIndex

    ceil(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.ceil)
    :   `ceil` rounds a floating point value to an integer towards positive infinity

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to round up
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `roundint.<size>(value)`

        Return type:
        :   ExpressionIndex

    compare_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_equal)
    :   `compare_equal` returns comparison expression of size `size` checking if expression `a`
        is equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    compare_not_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_not_equal)
    :   `compare_not_equal` returns comparison expression of size `size` checking if expression
        `a` is not equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    compare_signed_greater_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_signed_greater_equal)
    :   `compare_signed_greater_equal` returns comparison expression of size `size` checking if
        expression `a` is signed greater than or equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    compare_signed_greater_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_signed_greater_than)
    :   `compare_signed_greater_than` returns comparison expression of size `size` checking if
        expression `a` is signed greater than or equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    compare_signed_less_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_signed_less_equal)
    :   `compare_signed_less_equal` returns comparison expression of size `size` checking if
        expression `a` is signed less than or equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    compare_signed_less_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_signed_less_than)
    :   `compare_signed_less_than` returns comparison expression of size `size` checking if
        expression `a` is signed less than expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    compare_unsigned_greater_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_unsigned_greater_equal)
    :   `compare_unsigned_greater_equal` returns comparison expression of size `size` checking
        if expression `a` is unsigned greater than or equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    compare_unsigned_greater_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_unsigned_greater_than)
    :   `compare_unsigned_greater_than` returns comparison expression of size `size` checking if
        expression `a` is unsigned greater than or equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    compare_unsigned_less_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_unsigned_less_equal)
    :   `compare_unsigned_less_equal` returns comparison expression of size `size` checking if
        expression `a` is unsigned less than or equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    compare_unsigned_less_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.compare_unsigned_less_than)
    :   `compare_unsigned_less_than` returns comparison expression of size `size` checking if
        expression `a` is unsigned less than expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – LHS of comparison
            - **b** (*ExpressionIndex*) – RHS of comparison
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a comparison expression.

        Return type:
        :   ExpressionIndex

    const(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.const)
    :   `const` returns an expression for the constant integer `value` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the constant in bytes
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value of the constant
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    const_data(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.const_data)
    :   `const_data` returns an expression for the constant data `data`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the data
            - **data** ([*ConstantData*](variable.md#binaryninja.variable.ConstantData
              "binaryninja.variable.ConstantData")) – value of the data
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    const_pointer(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.const_pointer)
    :   `const_pointer` returns an expression for the constant pointer `value` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the pointer in bytes
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address referenced by the pointer
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    copy_expr(*original: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.copy_expr)
    :   `copy_expr` makes a shallow copy of the given IL expression, adding a new expression to
        the IL function.

        Warning

        The copy will not copy any child expressions, but will instead reference them as well
        (by expression index). This means that you cannot use this function to copy an
        expression tree to another function. If you want to copy an expression tree, you should
        use
        [`MediumLevelILFunction.copy_expr_to`](#binaryninja.mediumlevelil.MediumLevelILFunction.copy_expr_to
        "binaryninja.mediumlevelil.MediumLevelILFunction.copy_expr_to"). Metadata such as
        expression type and attributes are also not copied.

        Parameters:
        :   **original**
            ([*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction")) – the original IL Instruction you
            want to copy

        Returns:
        :   The index of the newly copied expression

        Return type:
        :   ExpressionIndex

    copy_expr_to(*expr: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*, *dest: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *sub_expr_handler: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")], ExpressionIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.copy_expr_to)
    :   `copy_expr_to` deep copies an expression from this function into a target function If
        provided, the function `sub_expr_handler` will be called on every copied sub-expression

        Warning

        This function should ONLY be called as a part of a lifter or workflow. It will otherwise
        not do anything useful as analysis will not be running.

        Parameters:
        :   - **expr**
              ([*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction")) – Expression in this function to
              copy
            - **dest** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) – Function to copy the expression to
            - **sub_expr_handler**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction")*]**,* *ExpressionIndex**]* *|*
              *None*) – Optional function to call on every copied sub-expression

        Returns:
        :   Index of the copied expression in the target function

        Return type:
        :   ExpressionIndex

    create_graph(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreFlowGraph](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.create_graph)
    :   Parameters:
        :   **settings**
            ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*CoreFlowGraph*](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph
            "binaryninja.flowgraph.CoreFlowGraph")

    create_graph_immediate(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreFlowGraph](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.create_graph_immediate)
    :   Parameters:
        :   **settings**
            ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*CoreFlowGraph*](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph
            "binaryninja.flowgraph.CoreFlowGraph")

    div_double_prec_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.div_double_prec_signed)
    :   `div_double_prec_signed` signed divides double precision expression `a` by expression
        `b` and returns an expression. The first operand is of size `2*size` bytes and the other
        operand and return value are of size `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `divs.dp.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    div_double_prec_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.div_double_prec_unsigned)
    :   `div_double_prec_unsigned` unsigned divides double precision expression `a` by
        expression `b` and returns an expression. The first operand is of size `2*size` bytes
        and the other operand and return value are of size `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `divu.dp.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    div_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.div_signed)
    :   `div_signed` signed divides expression `a` by expression `b` and returns an expression.
        Both the operands and return value are `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `divs.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    div_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.div_unsigned)
    :   `div_unsigned` unsigned divides expression `a` by expression `b` and returns an
        expression. Both the operands and return value are `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `divu.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    expr(*operation: [MediumLevelILOperation](enums.md#binaryninja.enums.MediumLevelILOperation "binaryninja.enums.MediumLevelILOperation")*, *a: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *b: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *c: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *d: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *e: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *source_location: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.expr)
    :   Parameters:
        :   - **operation**
              ([*MediumLevelILOperation*](enums.md#binaryninja.enums.MediumLevelILOperation
              "binaryninja.enums.MediumLevelILOperation")) –
            - **a** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **b** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **c** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **d** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **e** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **source_location**
              ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation") *|* *None*) –

        Return type:
        :   ExpressionIndex

    extern_pointer(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.extern_pointer)
    :   `extern_pointer` returns an expression for the external pointer `value` at offset
        `offset` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the pointer in bytes
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address referenced by the pointer
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset applied to the address
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation") *|* *None*) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    finalize() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.finalize)
    :   `finalize` ends the function and computes the list of basic blocks.

        Return type:
        :   *None*

    float_abs(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_abs)
    :   `float_abs` returns absolute value of floating point expression `value` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to get the absolute value of
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fabs.<size>(value)`

        Return type:
        :   ExpressionIndex

    float_add(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_add)
    :   `float_add` adds floating point expression `a` to expression `b` and returning an
        expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fadd.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    float_compare_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_compare_equal)
    :   `float_compare_equal` returns floating point comparison expression of size `size`
        checking if expression `a` is equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the operands in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `a f== b`

        Return type:
        :   ExpressionIndex

    float_compare_greater_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_compare_greater_equal)
    :   `float_compare_greater_equal` returns floating point comparison expression of size
        `size` checking if expression `a` is greater than or equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the operands in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `a f>= b`

        Return type:
        :   ExpressionIndex

    float_compare_greater_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_compare_greater_than)
    :   `float_compare_greater_than` returns floating point comparison expression of size `size`
        checking if expression `a` is greater than expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the operands in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `a f> b`

        Return type:
        :   ExpressionIndex

    float_compare_less_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_compare_less_equal)
    :   `float_compare_less_equal` returns floating point comparison expression of size `size`
        checking if expression `a` is less than or equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the operands in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `a f<= b`

        Return type:
        :   ExpressionIndex

    float_compare_less_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_compare_less_than)
    :   `float_compare_less_than` returns floating point comparison expression of size `size`
        checking if expression `a` is less than expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the operands in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `a f< b`

        Return type:
        :   ExpressionIndex

    float_compare_not_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_compare_not_equal)
    :   `float_compare_not_equal` returns floating point comparison expression of size `size`
        checking if expression `a` is not equal to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the operands in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `a f!= b`

        Return type:
        :   ExpressionIndex

    float_compare_ordered(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_compare_ordered)
    :   `float_compare_ordered` returns floating point comparison expression of size `size`
        checking if expression `a` is ordered relative to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the operands in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `is_ordered(a, b)`

        Return type:
        :   ExpressionIndex

    float_compare_unordered(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_compare_unordered)
    :   `float_compare_unordered` returns floating point comparison expression of size `size`
        checking if expression `a` is unordered relative to expression `b`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the operands in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `is_unordered(a, b)`

        Return type:
        :   ExpressionIndex

    float_const_double(*value: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_const_double)
    :   `float_const_double` returns an expression for the double precision floating point value
        `value`

        Parameters:
        :   - **value** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python
              v3.14)")) – float value for the constant
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    float_const_raw(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_const_raw)
    :   `float_const_raw` returns an expression for the constant raw binary floating point value
        `value` with size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the constant in bytes
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value for the raw binary representation of the constant
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    float_const_single(*value: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_const_single)
    :   `float_const_single` returns an expression for the single precision floating point value
        `value`

        Parameters:
        :   - **value** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python
              v3.14)")) – float value for the constant
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    float_convert(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_convert)
    :   `int_to_float` converts floating point value of expression `value` to size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to negate
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fconvert.<size>(value)`

        Return type:
        :   ExpressionIndex

    float_div(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_div)
    :   `float_div` divides floating point expression `a` by expression `b` and returning an
        expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fdiv.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    float_mult(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_mult)
    :   `float_mult` multiplies floating point expression `a` by expression `b` and returning an
        expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fmul.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    float_neg(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_neg)
    :   `float_neg` returns sign negation of floating point expression `value` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to negate
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fneg.<size>(value)`

        Return type:
        :   ExpressionIndex

    float_sqrt(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_sqrt)
    :   `float_sqrt` returns square root of floating point expression `value` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to calculate the square root of
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `sqrt.<size>(value)`

        Return type:
        :   ExpressionIndex

    float_sub(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_sub)
    :   `float_sub` subtracts floating point expression `b` from expression `a` and returning an
        expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fsub.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    float_to_int(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_to_int)
    :   `float_to_int` returns integer value of floating point expression `value` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to convert to an int
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `int.<size>(value)`

        Return type:
        :   ExpressionIndex

    float_trunc(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.float_trunc)
    :   `float_trunc` rounds a floating point value to an integer towards zero

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to truncate
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `roundint.<size>(value)`

        Return type:
        :   ExpressionIndex

    floor(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.floor)
    :   `floor` rounds a floating point value to an integer towards negative infinity

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to round down
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `roundint.<size>(value)`

        Return type:
        :   ExpressionIndex

    force_ver(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *dest: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *src: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.force_ver)
    :   `force_ver` creates a new version of the variable `dest` in `src` Effectively, this is
        like saying src = dest, which analysis can then use as a new variable definition site.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the variable
            - **dest** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable to force a new version of
            - **src** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable created with the new version
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `FORCE_VER(reg)`

        Return type:
        :   ExpressionIndex

    free_var_slot(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.free_var_slot)
    :   `free_var_slot` return an expression that clears the slot of the variable `var` which is
        in a register stack

        Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – variable to free
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the expression `free_var_slot(var)`

        Return type:
        :   ExpressionIndex

    generate_ssa_form(*analyze_conditionals: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *handle_aliases: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *known_not_aliases: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *known_aliases: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.generate_ssa_form)
    :   `generate_ssa_form` generate SSA form given the current MLIL

        Parameters:
        :   - **analyze_conditionals** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – whether or not to analyze conditionals, defaults to `True`
            - **handle_aliases** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in
              Python v3.14)")) – whether or not to handle aliases, defaults to `True`
            - **known_not_aliases** ([*list*](https://docs.python.org/3/library/stdtypes.html#list
              "(in Python v3.14)")*(*[*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")*)*) – optional list of variables known to be not
              aliased
            - **known_aliases** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in
              Python v3.14)")*(*[*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")*)*) – optional list of variables known to be aliased

        Return type:
        :   *None*

    get_basic_block_at(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [MediumLevelILBasicBlock](#binaryninja.mediumlevelil.MediumLevelILBasicBlock "binaryninja.mediumlevelil.MediumLevelILBasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_basic_block_at)
    :   `get_basic_block_at` returns the BasicBlock at the given MLIL instruction `index`.

        Parameters:
        :   **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Index of the MLIL instruction of the BasicBlock to retrieve.

        Example:
        :   ```
            >>> current_il_function.get_basic_block_at(current_il_index)
            <mlil block: x86@40-60>
            ```

        Return type:
        :   [*MediumLevelILBasicBlock*](#binaryninja.mediumlevelil.MediumLevelILBasicBlock
            "binaryninja.mediumlevelil.MediumLevelILBasicBlock") | *None*

    get_expr(*index: ExpressionIndex*) → [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_expr)
    :   `get_expr` retrieves the IL expression at a given expression index in the function.

        Warning

        Not all IL expressions are valid, even if their index is within the bounds of the
        function, they might not be used by the function and might not contain properly
        structured data.

        Parameters:
        :   **index** (*ExpressionIndex*) – Index of desired expression in function

        Returns:
        :   A MediumLevelILInstruction object for the expression, if it exists. Otherwise, None

        Return type:
        :   [*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction") | *None*

    get_expr_count() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_expr_count)
    :   `get_expr_count` gives a the total number of expressions in this IL function

        You can use this to enumerate all expressions in conjunction with
        [`get_expr`](#binaryninja.mediumlevelil.MediumLevelILFunction.get_expr
        "binaryninja.mediumlevelil.MediumLevelILFunction.get_expr")

        Warning

        Not all IL expressions are valid, even if their index is within the bounds of the
        function, they might not be used by the function and might not contain properly
        structured data.

        Returns:
        :   The number of expressions in the function

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_expr_index_for_instruction(*instr: InstructionIndex*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_expr_index_for_instruction)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   ExpressionIndex

    get_expr_type(*expr_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_expr_type)
    :   Get type of expression

        Parameters:
        :   **expr_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – index of the expression to retrieve

        Return type:
        :   *Optional*[’types.Type’]

    get_high_level_il_expr_index(*expr: ExpressionIndex*) → ExpressionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_high_level_il_expr_index)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   ExpressionIndex | *None*

    get_high_level_il_expr_indexes(*expr: ExpressionIndex*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex][[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_high_level_il_expr_indexes)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[ExpressionIndex]

    get_high_level_il_instruction_index(*instr: InstructionIndex*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_high_level_il_instruction_index)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   InstructionIndex | *None*

    get_instruction_index_for_expr(*expr: ExpressionIndex*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_instruction_index_for_expr)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   InstructionIndex | *None*

    get_instruction_start(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_instruction_start)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –

        Return type:
        :   InstructionIndex | *None*

    get_label_for_source_instruction(*i: InstructionIndex*) → [MediumLevelILLabel](#binaryninja.mediumlevelil.MediumLevelILLabel "binaryninja.mediumlevelil.MediumLevelILLabel") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_label_for_source_instruction)
    :   Get the MediumLevelILLabel for a given source instruction. The source instruction must
        be at the start of a basic block in the source function passed to
        [`prepare_to_copy_function`](#binaryninja.mediumlevelil.MediumLevelILFunction.prepare_to_copy_function
        "binaryninja.mediumlevelil.MediumLevelILFunction.prepare_to_copy_function"). The label
        will be marked resolved when its source block is passed to
        [`prepare_to_copy_block`](#binaryninja.mediumlevelil.MediumLevelILFunction.prepare_to_copy_block
        "binaryninja.mediumlevelil.MediumLevelILFunction.prepare_to_copy_block").

        Warning

        The instruction index parameter for this pertains to the *source function* passed to
        prepare_to_copy_function, not the current function.

        Note

        The returned label is to an internal object with the same lifetime as the containing
        MediumLevelILFunction.

        Parameters:
        :   **i** (*InstructionIndex*) – The source instruction index

        Returns:
        :   The MediumLevelILLabel for the source instruction

        Return type:
        :   [*MediumLevelILLabel*](#binaryninja.mediumlevelil.MediumLevelILLabel
            "binaryninja.mediumlevelil.MediumLevelILLabel") | *None*

    get_live_instructions_for_var(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *include_last_use: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_live_instructions_for_var)
    :   `get_live_instructions_for_var` computes the list of instructions for which `var` is
        live. If `include_last_use` is False, the last use of the variable will not be included
        in the list (this allows for easier computation of overlaps in liveness between two
        variables). If the variable is never used, this function will return an empty list.

        Parameters:
        :   - **var** ([*SSAVariable*](#binaryninja.mediumlevelil.SSAVariable
              "binaryninja.mediumlevelil.SSAVariable")) – the variable to query
            - **include_last_use** ([*bool*](https://docs.python.org/3/library/functions.html#bool
              "(in Python v3.14)")) – whether to include the last use of the variable in the list of
              instructions

        Returns:
        :   list of instructions for which `var` is live

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")([*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction"))

    get_low_level_il_expr_index(*expr: ExpressionIndex*) → ExpressionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_low_level_il_expr_index)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   ExpressionIndex | *None*

    get_low_level_il_expr_indexes(*expr: ExpressionIndex*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex][[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_low_level_il_expr_indexes)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[ExpressionIndex]

    get_low_level_il_instruction_index(*instr: InstructionIndex*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_low_level_il_instruction_index)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   InstructionIndex | *None*

    get_non_ssa_instruction_index(*instr: InstructionIndex*) → InstructionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_non_ssa_instruction_index)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   InstructionIndex

    get_ssa_instruction_index(*instr: InstructionIndex*) → InstructionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_ssa_instruction_index)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   InstructionIndex

    get_ssa_memory_definition(*version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_ssa_memory_definition)
    :   Parameters:
        :   **version** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction") | *None*

    get_ssa_memory_uses(*version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_ssa_memory_uses)
    :   Parameters:
        :   **version** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction")]

    get_ssa_var_definition(*ssa_var: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [MediumLevelILVarSsa](#binaryninja.mediumlevelil.MediumLevelILVarSsa "binaryninja.mediumlevelil.MediumLevelILVarSsa")*) → [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_ssa_var_definition)
    :   Gets the instruction that contains the given SSA variable’s definition.

        Since SSA variables can only be defined once, this will return the single instruction
        where that occurs. For SSA variable version 0s, which don’t have definitions, this will
        return None instead.

        Parameters:
        :   **ssa_var** ([*SSAVariable*](#binaryninja.mediumlevelil.SSAVariable
            "binaryninja.mediumlevelil.SSAVariable") *|*
            [*MediumLevelILVarSsa*](#binaryninja.mediumlevelil.MediumLevelILVarSsa
            "binaryninja.mediumlevelil.MediumLevelILVarSsa")) –

        Return type:
        :   [*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction") | *None*

    get_ssa_var_uses(*ssa_var: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [MediumLevelILVarSsa](#binaryninja.mediumlevelil.MediumLevelILVarSsa "binaryninja.mediumlevelil.MediumLevelILVarSsa")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_ssa_var_uses)
    :   Gets all the instructions that use the given SSA variable.

        Parameters:
        :   **ssa_var** ([*SSAVariable*](#binaryninja.mediumlevelil.SSAVariable
            "binaryninja.mediumlevelil.SSAVariable") *|*
            [*MediumLevelILVarSsa*](#binaryninja.mediumlevelil.MediumLevelILVarSsa
            "binaryninja.mediumlevelil.MediumLevelILVarSsa")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction")]

    get_ssa_var_value(*ssa_var: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_ssa_var_value)
    :   Parameters:
        :   **ssa_var** ([*SSAVariable*](#binaryninja.mediumlevelil.SSAVariable
            "binaryninja.mediumlevelil.SSAVariable")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_var_definitions(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_var_definitions)
    :   Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction")]

    get_var_uses(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.get_var_uses)
    :   Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction")]

    goto(*label: [MediumLevelILLabel](#binaryninja.mediumlevelil.MediumLevelILLabel "binaryninja.mediumlevelil.MediumLevelILLabel")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.goto)
    :   `goto` returns a goto expression which jumps to the provided MediumLevelILLabel.

        Parameters:
        :   - **label** ([*MediumLevelILLabel*](#binaryninja.mediumlevelil.MediumLevelILLabel
              "binaryninja.mediumlevelil.MediumLevelILLabel")) – Label to jump to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the ExpressionIndex that jumps to the provided label

        Return type:
        :   ExpressionIndex

    if_expr(*operand: ExpressionIndex*, *t: [MediumLevelILLabel](#binaryninja.mediumlevelil.MediumLevelILLabel "binaryninja.mediumlevelil.MediumLevelILLabel")*, *f: [MediumLevelILLabel](#binaryninja.mediumlevelil.MediumLevelILLabel "binaryninja.mediumlevelil.MediumLevelILLabel")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.if_expr)
    :   `if_expr` returns the `if` expression which depending on condition `operand` jumps to
        the MediumLevelILLabel `t` when the condition expression `operand` is non-zero and `f`
        when it’s zero.

        Parameters:
        :   - **operand** (*ExpressionIndex*) – comparison expression to evaluate.
            - **t** ([*MediumLevelILLabel*](#binaryninja.mediumlevelil.MediumLevelILLabel
              "binaryninja.mediumlevelil.MediumLevelILLabel")) – Label for the true branch
            - **f** ([*MediumLevelILLabel*](#binaryninja.mediumlevelil.MediumLevelILLabel
              "binaryninja.mediumlevelil.MediumLevelILLabel")) – Label for the false branch
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the ExpressionIndex for the if expression

        Return type:
        :   ExpressionIndex

    imported_address(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.imported_address)
    :   `imported_address` returns an expression for an imported value with address `value` and
        size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the imported value
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address of the imported value
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    int_to_float(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.int_to_float)
    :   `int_to_float` returns floating point value of integer expression `value` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to convert to a float
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `float.<size>(value)`

        Return type:
        :   ExpressionIndex

    intrinsic(*outputs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*, *intrinsic: IntrinsicName | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | IntrinsicIndex*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.intrinsic)
    :   `intrinsic` return an intrinsic expression.

        Parameters:
        :   - **outputs** (*List**[*[*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")*]*) – list of output variables
            - **intrinsic** (*IntrinsicType*) – which intrinsic to call
            - **params** (*List**[**ExpressionIndex**]*) – parameters to intrinsic
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   an intrinsic expression.

        Return type:
        :   ExpressionIndex

    is_ssa_var_live(*ssa_var: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.is_ssa_var_live)
    :   `is_ssa_var_live` determines if `ssa_var` is live at any point in the function

        Parameters:
        :   **ssa_var** ([*SSAVariable*](#binaryninja.mediumlevelil.SSAVariable
            "binaryninja.mediumlevelil.SSAVariable")) – the SSA variable to query

        Returns:
        :   whether the variable is live at any point in the function

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_ssa_var_live_at(*ssa_var: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*, *instr: InstructionIndex*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.is_ssa_var_live_at)
    :   `is_ssa_var_live_at` determines if `ssa_var` is live at a given point in the function;
        counts phi’s as uses

        Parameters:
        :   - **ssa_var** ([*SSAVariable*](#binaryninja.mediumlevelil.SSAVariable
              "binaryninja.mediumlevelil.SSAVariable")) –
            - **instr** (*InstructionIndex*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_var_live_at(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *instr: InstructionIndex*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.is_var_live_at)
    :   `is_var_live_at` determines if `var` is live at a given point in the function

        Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) –
            - **instr** (*InstructionIndex*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    jump(*dest: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.jump)
    :   `jump` returns an expression which jumps (branches) to the expression `dest`

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression to jump to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `jump(dest)`

        Return type:
        :   ExpressionIndex

    jump_to(*dest: ExpressionIndex*, *targets: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [MediumLevelILLabel](#binaryninja.mediumlevelil.MediumLevelILLabel "binaryninja.mediumlevelil.MediumLevelILLabel")]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.jump_to)
    :   `jump_to` returns an expression which jumps (branches) various targets in `targets`
        choosing the target in `targets` based on the value calculated by `dest`

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression choosing which jump target to use
            - **targets** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping
              "(in Python v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*,* [*MediumLevelILLabel*](#binaryninja.mediumlevelil.MediumLevelILLabel
              "binaryninja.mediumlevelil.MediumLevelILLabel")*]*) – the list of targets for jump
              locations
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression
            - **targets** –

        Returns:
        :   The expression `jump(dest)`

        Return type:
        :   ExpressionIndex

    load(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.load)
    :   `load` Reads `size` bytes from the expression `src`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to read
            - **src** (*ExpressionIndex*) – the expression to read memory from
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `[addr].size`

        Return type:
        :   ExpressionIndex

    load_struct(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: ExpressionIndex*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.load_struct)
    :   `load_struct` Reads `size` bytes at the offset `offset` from the expression `src`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to read
            - **src** (*ExpressionIndex*) – the expression to read memory from
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of field in the memory
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `[(src + offset)].size` (often rendered `src->offset.size`)

        Return type:
        :   ExpressionIndex

    logical_shift_right(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.logical_shift_right)
    :   `logical_shift_right` logically right shifts expression `a` by expression `b` returning
        an expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `lsr.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    low_part(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.low_part)
    :   `low_part` truncates the expression in `value` to `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to zero extend
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `(value).<size>`

        Return type:
        :   ExpressionIndex

    mark_label(*label: [MediumLevelILLabel](#binaryninja.mediumlevelil.MediumLevelILLabel "binaryninja.mediumlevelil.MediumLevelILLabel")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.mark_label)
    :   `mark_label` assigns a MediumLevelILLabel to the current IL address.

        Parameters:
        :   **label** ([*MediumLevelILLabel*](#binaryninja.mediumlevelil.MediumLevelILLabel
            "binaryninja.mediumlevelil.MediumLevelILLabel")) –

        Return type:
        :   *None*

    mod_double_prec_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.mod_double_prec_signed)
    :   `mod_double_prec_signed` signed modulus double precision expression `a` by expression
        `b` and returns an expression. The first operand is of size `2*size` bytes and the other
        operand and return value are of size `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `mods.dp.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    mod_double_prec_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.mod_double_prec_unsigned)
    :   `mod_double_prec_unsigned` unsigned modulus double precision expression `a` by
        expression `b` and returns an expression. The first operand is of size `2*size` bytes
        and the other operand and return value are of size `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `modu.dp.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    mod_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.mod_signed)
    :   `mod_signed` signed modulus expression `a` by expression `b` and returns an expression.
        Both the operands and return value are `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `mods.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    mod_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.mod_unsigned)
    :   `mod_unsigned` unsigned modulus expression `a` by expression `b` and returns an
        expression. Both the operands and return value are `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `modu.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    mult(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.mult)
    :   `mult` multiplies expression `a` by expression `b` and returns an expression. Both the
        operands and return value are `size` bytes as the product’s upper half is discarded.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `mult.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    mult_double_prec_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.mult_double_prec_signed)
    :   `mult_double_prec_signed` signed multiplies expression `a` by expression `b` and returns
        an expression. Both the operands are `size` bytes and the returned expression is of size
        `2*size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `muls.dp.<2*size>(a, b)`

        Return type:
        :   ExpressionIndex

    mult_double_prec_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.mult_double_prec_unsigned)
    :   `mult_double_prec_unsigned` unsigned multiplies expression `a` by expression `b` and
        returnisan expression. Both the operands are `size` bytes and the returned expression is
        of size `2*size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `mulu.dp.<2*size>(a, b)`

        Return type:
        :   ExpressionIndex

    neg_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.neg_expr)
    :   `neg_expr` two’s complement sign negation of expression `value` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to negate
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `neg.<size>(value)`

        Return type:
        :   ExpressionIndex

    no_ret(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.no_ret)
    :   `no_ret` returns an expression that halts execution

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `noreturn`

        Return type:
        :   ExpressionIndex

    nop(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.nop)
    :   `nop` no operation, this instruction does nothing

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation") *|* *None*) – Location of expression

        Returns:
        :   The no operation expression

        Return type:
        :   ExpressionIndex

    not_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.not_expr)
    :   `not_expr` bitwise inversion of expression `value` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to bitwise invert
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `not.<size>(value)`

        Return type:
        :   ExpressionIndex

    or_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.or_expr)
    :   `or_expr` bitwise or’s expression `a` and expression `b` returning an expression of
        `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `or.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    prepare_to_copy_block(*src: [MediumLevelILBasicBlock](#binaryninja.mediumlevelil.MediumLevelILBasicBlock "binaryninja.mediumlevelil.MediumLevelILBasicBlock")*)[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.prepare_to_copy_block)
    :   `prepare_to_copy_block` sets up state when copying a function in preparation of copying
        the instructions from the block `src` It enables use of
        [`get_label_for_source_instruction`](#binaryninja.mediumlevelil.MediumLevelILFunction.get_label_for_source_instruction
        "binaryninja.mediumlevelil.MediumLevelILFunction.get_label_for_source_instruction")
        during function transformation.

        Parameters:
        :   **src** ([*MediumLevelILBasicBlock*](#binaryninja.mediumlevelil.MediumLevelILBasicBlock
            "binaryninja.mediumlevelil.MediumLevelILBasicBlock")) – block about to be copied from

    prepare_to_copy_function(*src: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*)[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.prepare_to_copy_function)
    :   `prepare_to_copy_function` sets up state in this MLIL function in preparation of copying
        instructions from `src` It enables use of
        [`get_label_for_source_instruction`](#binaryninja.mediumlevelil.MediumLevelILFunction.get_label_for_source_instruction
        "binaryninja.mediumlevelil.MediumLevelILFunction.get_label_for_source_instruction")
        during function transformation.

        Parameters:
        :   **src** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
            "binaryninja.mediumlevelil.MediumLevelILFunction")) – function about to be copied from

    replace_expr(*original: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | ExpressionIndex | InstructionIndex*, *new: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | ExpressionIndex | InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.replace_expr)
    :   `replace_expr` replace an existing IL instruction in-place with another one

        Both expressions must have been created on the same function. The original expression
        will be replaced completely and the new expression will not be modified.

        Parameters:
        :   - **original** (*ExpressionIndex*) – the ExpressionIndex to replace (may also be an
              expression index)
            - **new** (*ExpressionIndex*) – the ExpressionIndex to add to the current
              LowLevelILFunction (may also be an expression index)

        Return type:
        :   *None*

    ret(*sources: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.ret)
    :   `ret` returns an expression which jumps (branches) to the calling function, returning a
        result specified by the expressions in `sources`.

        Parameters:
        :   - **sources** (*List**[**ExpressionIndex**]*) – list of returned expressions
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `return sources...`

        Return type:
        :   ExpressionIndex

    rotate_left(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.rotate_left)
    :   `rotate_left` bitwise rotates left expression `a` by expression `b` returning an
        expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `rol.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    rotate_left_carry(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.rotate_left_carry)
    :   `rotate_left_carry` bitwise rotates left expression `a` by expression `b` with carry
        from `carry` returning an expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **carry** (*ExpressionIndex*) – Carried value expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `rlc.<size>(a, b, carry)`

        Return type:
        :   ExpressionIndex

    rotate_right(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.rotate_right)
    :   `rotate_right` bitwise rotates right expression `a` by expression `b` returning an
        expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `ror.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    rotate_right_carry(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.rotate_right_carry)
    :   `rotate_right_carry` bitwise rotates right expression `a` by expression `b` with carry
        from `carry` returning an expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **carry** (*ExpressionIndex*) – Carried value expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `rrc.<size>(a, b, carry)`

        Return type:
        :   ExpressionIndex

    round_to_int(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.round_to_int)
    :   `round_to_int` rounds a floating point value to the nearest integer

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to round to the nearest integer
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `roundint.<size>(value)`

        Return type:
        :   ExpressionIndex

    separate_param_list(*params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.separate_param_list)
    :   `separate_param_list` returns an expression which holds a list of parameters in `params`

        Parameters:
        :   - **params** (*List**[**ExpressionIndex**]*) – parameter expressions
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `separate_param_list(params...)`

        Return type:
        :   ExpressionIndex

    set_current_address(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.set_current_address)
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –

        Return type:
        :   *None*

    set_expr_attributes(*expr: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | ExpressionIndex | InstructionIndex*, *value: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ILInstructionAttribute](enums.md#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILInstructionAttribute](enums.md#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute")]*)[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.set_expr_attributes)
    :   `set_expr_attributes` allows modification of instruction attributes but ONLY during
        lifting.

        Warning

        This function should ONLY be called as a part of a lifter. It will otherwise not do
        anything useful as there’s no way to trigger re-analysis of IL levels at this time.

        Parameters:
        :   - **expr** (*ExpressionIndex*) – the ExpressionIndex to replace (may also be an expression
              index)
            - **value** ([*set*](https://docs.python.org/3/library/stdtypes.html#set "(in Python
              v3.14)")*(*[*ILInstructionAttribute*](enums.md#binaryninja.enums.ILInstructionAttribute
              "binaryninja.enums.ILInstructionAttribute")*)*) – the set of attributes to place on the
              instruction

        Return type:
        :   *None*

    set_expr_type(*expr_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *expr_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.set_expr_type)
    :   Set type of expression

        This API is only meant for workflows or for debugging purposes, since the changes they
        make are not persistent and get lost after a database save and reload. To make
        persistent changes to the analysis, one should use other APIs to, for example, change
        the type of variables. The analysis will then propagate the type of the variable and
        update the type of related expressions.

        Parameters:
        :   - **expr_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – index of the expression to set
            - **StringOrType** – new type of the expression
            - **expr_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*Type*](types.md#binaryninja.types.Type "binaryninja.types.Type") *|*
              [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")
              *|* *None*) –

        Return type:
        :   *None*

    set_var(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *dest: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.set_var)
    :   `set_var` sets the variable `dest` of size `size` to the expression `src`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the variable in bytes
            - **dest** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable being set
            - **src** (*ExpressionIndex*) – expression with the value to set the variable to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `dest = src`

        Return type:
        :   ExpressionIndex

    set_var_field(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *dest: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.set_var_field)
    :   `set_var_field` sets the field `offset` of variable `dest` of size `size` to the
        expression `src`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the field in bytes
            - **dest** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable being set
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of field in the variable
            - **src** (*ExpressionIndex*) – expression with the value to set the field to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `dest:offset = src`

        Return type:
        :   ExpressionIndex

    set_var_split(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *hi: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *lo: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.set_var_split)
    :   `set_var_split` uses `hi` and `lo` as a single extended variable of size `2*size`
        setting `hi:lo` to the expression `src`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of each variable in bytes
            - **hi** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the high variable being set
            - **lo** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the low variable being set
            - **src** (*ExpressionIndex*) – expression with the value to set the variables to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `hi:lo = src`

        Return type:
        :   ExpressionIndex

    shared_param_slot(*params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.shared_param_slot)
    :   `shared_param_slot` returns an expression which holds a list of parameters in `params`
        that are stored in a shared parameter slot

        Parameters:
        :   - **params** (*List**[**ExpressionIndex**]*) – parameter expressions
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `shared_param_slot(params...)`

        Return type:
        :   ExpressionIndex

    shift_left(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.shift_left)
    :   `shift_left` left shifts expression `a` by expression `b` returning an expression of
        `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `lsl.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    sign_extend(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.sign_extend)
    :   `sign_extend` two’s complement sign-extends the expression in `value` to `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to sign extend
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `sx.<size>(value)`

        Return type:
        :   ExpressionIndex

    store(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *dest: ExpressionIndex*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.store)
    :   `store` Writes `size` bytes to expression `dest` read from expression `src`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to write
            - **dest** (*ExpressionIndex*) – the expression to write to
            - **src** (*ExpressionIndex*) – the expression to be written
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `[dest].size = src`

        Return type:
        :   ExpressionIndex

    store_struct(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *dest: ExpressionIndex*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.store_struct)
    :   `store_struct` Writes `size` bytes to expression `dest` at the offset `offset` read from
        expression `src`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to write
            - **dest** (*ExpressionIndex*) – the expression to write to
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of field in the memory
            - **src** (*ExpressionIndex*) – the expression to be written
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `[(dest + offset)].size = src` (often rendered `dest->offset.size`)

        Return type:
        :   ExpressionIndex

    sub(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.sub)
    :   `sub` subtracts expression `a` to expression `b` returning an expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `sub.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    sub_borrow(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.sub_borrow)
    :   `sub_borrow` subtracts expression `a` to expression `b` with borrow from `carry`
        returning an expression of `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **carry** (*ExpressionIndex*) – Carried value expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `sbb.<size>(a, b, carry)`

        Return type:
        :   ExpressionIndex

    system_call(*output: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.system_call)
    :   `system_call` returns an expression which performs a system call with the parameters
        defined in `params` returning values in the variables in `output`.

        Parameters:
        :   - **output** (*List**[**'variable.Variable'**]*) – output variables
            - **params** (*List**[**ExpressionIndex**]*) – parameter variables
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `output = syscall(dest, params...)`

        Return type:
        :   ExpressionIndex

    system_call_untyped(*output: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *stack: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.system_call_untyped)
    :   `system_call_untyped` returns an expression which performs a system call with the
        parameters defined in `params` returning values in the variables in `output` where stack
        resolution could not be determined and the top of the stack has to be specified in
        `stack`

        Parameters:
        :   - **output** (*List**[**'variable.Variable'**]*) – output variables
            - **params** (*List**[**ExpressionIndex**]*) – parameter variables
            - **stack** (*ExpressionIndex*) – expression of top of stack
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `output = syscall(dest, params..., stack = stack)`

        Return type:
        :   ExpressionIndex

    tailcall(*output: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*, *dest: ExpressionIndex*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.tailcall)
    :   `tailcall` returns an expression which tailcalls the function in the expression `dest`
        with the parameters defined in `params` returning values in the variables in `output`.

        Parameters:
        :   - **output** (*List**[**'variable.Variable'**]*) – output variables
            - **dest** (*ExpressionIndex*) – the expression to call
            - **params** (*List**[**ExpressionIndex**]*) – parameter variables
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `output = tailcall(dest, params...)`

        Return type:
        :   ExpressionIndex

    tailcall_untyped(*output: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*, *dest: ExpressionIndex*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *stack: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.tailcall_untyped)
    :   `tailcall_untyped` returns an expression which tailcalls the function in the expression
        `dest` with the parameters defined in `params` returning values in the variables in
        `output` where stack resolution could not be determined and the top of the stack has to
        be specified in `stack`

        Parameters:
        :   - **output** (*List**[**'variable.Variable'**]*) – output variables
            - **dest** (*ExpressionIndex*) – the expression to call
            - **params** (*List**[**ExpressionIndex**]*) – parameter variables
            - **stack** (*ExpressionIndex*) – expression of top of stack
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `output = tailcall(dest, params..., stack = stack)`

        Return type:
        :   ExpressionIndex

    test_bit(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.test_bit)
    :   `test_bit` returns an expression of size `size` that tells whether expression `a` has
        its bit with an index of the expression `b` is set

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes
            - **a** (*ExpressionIndex*) – an expression to be tested
            - **b** (*ExpressionIndex*) – an expression for the index of the big
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the result expression.

        Return type:
        :   ExpressionIndex

    translate(*expr_handler: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction"), [MediumLevelILBasicBlock](#binaryninja.mediumlevelil.MediumLevelILBasicBlock "binaryninja.mediumlevelil.MediumLevelILBasicBlock"), [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")], ExpressionIndex]*) → [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.translate)
    :   `translate` clones an IL function and modifies its expressions as specified by a given
        `expr_handler`, returning the updated IL function.

        Parameters:
        :   **expr_handler**
            ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
            v3.14)")*[**[*[*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
            "binaryninja.mediumlevelil.MediumLevelILFunction")*,*
            [*MediumLevelILBasicBlock*](#binaryninja.mediumlevelil.MediumLevelILBasicBlock
            "binaryninja.mediumlevelil.MediumLevelILBasicBlock")*,*
            [*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction")*]**,* *ExpressionIndex**]*) –

            Function to modify an expression and copy it to the new function. The function should
            have the following signature:

            expr_handler(new_func: MediumLevelILFunction, old_block: MediumLevelILBasicBlock,
            old_instr: MediumLevelILInstruction) -> ExpressionIndex

            Where:
            :   - **new_func** (*MediumLevelILFunction*): New function to receive translated
            instructions
            - **old_block** (*MediumLevelILBasicBlock*): Original block containing old_instr
            - **old_instr** (*MediumLevelILInstruction*): Original instruction
            - **returns** (*ExpressionIndex*): Expression index of newly created instruction in
            `new_func`

        Returns:
        :   Cloned IL function with modifications

        Return type:
        :   [*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
            "binaryninja.mediumlevelil.MediumLevelILFunction")

    trap(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.trap)
    :   `trap` returns a processor trap (interrupt) expression of the given integer `value`.

        Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – trap (interrupt) number
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a trap expression.

        Return type:
        :   ExpressionIndex

    traverse(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, **args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, ***kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.traverse)
    :   `traverse` iterates through all the instructions in the MediumLevelILInstruction and
        calls the callback function for each instruction and sub-instruction. See the [Developer
        Docs](https://docs.binary.ninja/dev/concepts.html#walking-ils) for more examples.

        Parameters:
        :   - **cb** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in
              Python
              v3.14)")*[**[*[*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction")*,*
              [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
              v3.14)")*]**,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")*]*) – Callback function that takes a HighLevelILInstruction and returns
              a value
            - **args** (*Any*) – Custom user-defined arguments
            - **kwargs** (*Any*) – Custom user-defined keyword arguments
            - **cb** –

        Returns:
        :   An iterator of the results of the callback function

        Return type:
        :   *Iterator*[*Any*]

        Example:
        :   ```
            >>> def find_constants(instr) -> Optional[int]:
            ...     if isinstance(instr, Constant):
            ...         return instr.constant
            >>> print(list(current_il_function.traverse(find_constants)))
            ```

    undefined(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.undefined)
    :   `undefined` returns the undefined expression. This should be used for instructions which
        perform functions but aren’t important for dataflow or partial emulation purposes.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the undefined expression.

        Return type:
        :   ExpressionIndex

    unimplemented(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.unimplemented)
    :   `unimplemented` returns the unimplemented expression. This should be used for all
        instructions which aren’t implemented.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the unimplemented expression.

        Return type:
        :   ExpressionIndex

    unimplemented_memory_ref(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *addr: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.unimplemented_memory_ref)
    :   `unimplemented_memory_ref` a memory reference to expression `addr` of size `size` with
        unimplemented operation.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size in bytes of the memory reference
            - **addr** (*ExpressionIndex*) – expression to reference memory
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the unimplemented memory reference expression.

        Return type:
        :   ExpressionIndex

    var(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.var)
    :   `var` returns the variable `src` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the variable in bytes
            - **src** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable being read
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   An expression for the given variable

        Return type:
        :   ExpressionIndex

    var_field(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.var_field)
    :   `var_field` returns the field at offset `offset` from variable `src` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the field in bytes
            - **src** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable being read
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of field in the variable
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `var:offset.size`

        Return type:
        :   ExpressionIndex

    var_split(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *hi: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *lo: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.var_split)
    :   `var_split` combines variables `hi` and `lo` of size `size` into an expression of size
        `2*size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of each variable in bytes
            - **hi** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable holding high part of value
            - **lo** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – the variable holding low part of value
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `hi:lo`

        Return type:
        :   ExpressionIndex

    visit(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.visit)
    :   Iterates over all the instructions in the function and calls the callback function for
        each instruction and each sub-instruction.

        Parameters:
        :   **cb** (*MediumLevelILVisitorCallback*) – Callback function that takes the name of the
            operand, the operand, operand type, and parent instruction

        Returns:
        :   True if all instructions were visited, False if the callback function returned False.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`MediumLevelILFunction.traverse`](#binaryninja.mediumlevelil.MediumLevelILFunction.traverse
        "binaryninja.mediumlevelil.MediumLevelILFunction.traverse") instead.

    visit_all(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.visit_all)
    :   Iterates over all the instructions in the function and calls the callback function for
        each instruction and their operands.

        Parameters:
        :   **cb** (*MediumLevelILVisitorCallback*) – Callback function that takes the name of the
            operand, the operand, operand type, and parent instruction

        Returns:
        :   True if all instructions were visited, False if the callback function returned False.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`MediumLevelILFunction.traverse`](#binaryninja.mediumlevelil.MediumLevelILFunction.traverse
        "binaryninja.mediumlevelil.MediumLevelILFunction.traverse") instead.

    visit_operands(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.visit_operands)
    :   Iterates over all the instructions in the function and calls the callback function for each operand and
        :   the operands of each sub-instruction.

        Parameters:
        :   **cb** (*MediumLevelILVisitorCallback*) – Callback function that takes the name of the
            operand, the operand, operand type, and parent instruction

        Returns:
        :   True if all instructions were visited, False if the callback function returned False.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`MediumLevelILFunction.traverse`](#binaryninja.mediumlevelil.MediumLevelILFunction.traverse
        "binaryninja.mediumlevelil.MediumLevelILFunction.traverse") instead.

    xor_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.xor_expr)
    :   `xor_expr` xor’s expression `a` and expression `b` returning an expression of `size`
        bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `xor.<size>(a, b)`

        Return type:
        :   ExpressionIndex

    zero_extend(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILFunction.zero_extend)
    :   `zero_extend` zero-extends the expression in `value` to `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to zero extend
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `zx.<size>(value)`

        Return type:
        :   ExpressionIndex

    *property* aliased_vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   This returns a list of Variables that are taken reference to and used elsewhere. You may
        also wish to consider MediumLevelIlFunction.vars and
        MediumLevelIlFunction.source_function.parameter_vars

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    *property* basic_blocks*: [MediumLevelILBasicBlockList](function.md#binaryninja.function.MediumLevelILBasicBlockList "binaryninja.function.MediumLevelILBasicBlockList")*

    *property* current_address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Current IL Address (read/write)

    *property* high_level_il*: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   High level IL for this medium level IL.

    *property* hlil*: [HighLevelILFunction](highlevelil.md#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* il_form*: [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType")*

    *property* instructions*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of mlil instructions of the current function

    *property* llil*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Alias for low_level_il

    *property* low_level_il*: [LowLevelILFunction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Low level IL for this function

    *property* non_ssa_form*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Medium level IL in non-SSA (default) form (read-only)

    *property* source_function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*

    *property* ssa_form*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Medium level IL in SSA form (read-only)

    *property* ssa_vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   This gets just the MLIL SSA variables - you may be interested in the union of
        MediumLevelIlFunction.aliased_vars and
        MediumLevelIlFunction.source_function.parameter_vars for all the variables used in the
        function

    *property* vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   This gets just the MLIL variables - you may be interested in the union of
        MediumLevelIlFunction.aliased_vars and
        MediumLevelIlFunction.source_function.parameter_vars for all the variables used in the
        function

    *property* view*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*

## MediumLevelILGoto

*class* MediumLevelILGoto[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILGoto)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    MediumLevelILGoto(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: InstructionIndex*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILIf

*class* MediumLevelILIf[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILIf)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    MediumLevelILIf(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* condition*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    *property* false*: InstructionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* true*: InstructionIndex*

## MediumLevelILImport

*class* MediumLevelILImport[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILImport)
:   Bases: [`MediumLevelILConstBase`](#binaryninja.mediumlevelil.MediumLevelILConstBase
    "binaryninja.mediumlevelil.MediumLevelILConstBase")

    MediumLevelILImport(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILInstruction

*class* MediumLevelILInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction)
:   Bases: [`BaseILInstruction`](commonil.md#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    `class MediumLevelILInstruction` Medium Level Intermediate Language Instructions are
    infinite length tree-based instructions. Tree-based instructions use infix notation with
    the left hand operand being the destination operand. Infix notation is thus more natural
    to read than other notations (e.g. x86 `mov eax, 0` vs. MLIL `eax = 0`).

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    copy_to(*dest: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *sub_expr_handler: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")], ExpressionIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.copy_to)
    :   `copy_to` deep copies an expression into a new IL function. If provided, the function
        `sub_expr_handler` will be called on every copied sub-expression

        Warning

        This function should ONLY be called as a part of a lifter or workflow. It will otherwise
        not do anything useful as analysis will not be running.

        Parameters:
        :   - **dest** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) – Function to copy the expression to
            - **sub_expr_handler**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction")*]**,* *ExpressionIndex**]* *|*
              *None*) – Optional function to call on every copied sub-expression

        Returns:
        :   Index of the copied expression in the target function

        Return type:
        :   ExpressionIndex

    *classmethod* create(*func: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.create)
    :   Parameters:
        :   - **func** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   [*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
            "binaryninja.mediumlevelil.MediumLevelILInstruction")

    get_branch_dependence(*branch_instr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [ILBranchDependence](enums.md#binaryninja.enums.ILBranchDependence "binaryninja.enums.ILBranchDependence")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_branch_dependence)
    :   Parameters:
        :   **branch_instr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) –

        Return type:
        :   [*ILBranchDependence*](enums.md#binaryninja.enums.ILBranchDependence
            "binaryninja.enums.ILBranchDependence")

    get_flag_value(*flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_flag_value)
    :   Parameters:
        :   **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
            "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_flag_value_after(*flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_flag_value_after)
    :   Parameters:
        :   **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
            "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_possible_flag_values(*flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_possible_flag_values)
    :   Parameters:
        :   - **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
              "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_flag_values_after(*flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_possible_flag_values_after)
    :   Parameters:
        :   - **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
              "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_reg_values(*reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_possible_reg_values)
    :   Parameters:
        :   - **reg** (*RegisterName* *|*
              [*ILRegister*](lowlevelil.md#binaryninja.lowlevelil.ILRegister
              "binaryninja.lowlevelil.ILRegister") *|* *RegisterIndex*) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_reg_values_after(*reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_possible_reg_values_after)
    :   Parameters:
        :   - **reg** (*RegisterName* *|*
              [*ILRegister*](lowlevelil.md#binaryninja.lowlevelil.ILRegister
              "binaryninja.lowlevelil.ILRegister") *|* *RegisterIndex*) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_stack_contents(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_possible_stack_contents)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_stack_contents_after(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_possible_stack_contents_after)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_values(*options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_possible_values)
    :   Parameters:
        :   **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
            "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_reg_value(*reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_reg_value)
    :   Parameters:
        :   **reg** (*RegisterName* *|*
            [*ILRegister*](lowlevelil.md#binaryninja.lowlevelil.ILRegister
            "binaryninja.lowlevelil.ILRegister") *|* *RegisterIndex*) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_reg_value_after(*reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_reg_value_after)
    :   Parameters:
        :   **reg** (*RegisterName* *|*
            [*ILRegister*](lowlevelil.md#binaryninja.lowlevelil.ILRegister
            "binaryninja.lowlevelil.ILRegister") *|* *RegisterIndex*) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_split_var_for_definition(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_split_var_for_definition)
    :   Gets the unique variable for a definition instruction. This unique variable can be
        passed to `Function.split_var` to split a variable at a definition. The given `var` is
        the assigned variable to query.

        Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) – variable to query

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")

    get_ssa_var_possible_values(*ssa_var: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] = []*)[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_ssa_var_possible_values)
    :   Parameters:
        :   - **ssa_var** ([*SSAVariable*](#binaryninja.mediumlevelil.SSAVariable
              "binaryninja.mediumlevelil.SSAVariable")) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]*) –

    get_ssa_var_version(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_ssa_var_version)
    :   Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_ssa_var_version_after(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_ssa_var_version_after)
    :   Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_stack_contents(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_stack_contents)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_stack_contents_after(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_stack_contents_after)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_var_for_flag(*flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_var_for_flag)
    :   Parameters:
        :   **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
            "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*) –

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")

    get_var_for_flag_after(*flag: FlagName | [ILFlag](lowlevelil.md#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | FlagIndex*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_var_for_flag_after)
    :   Parameters:
        :   **flag** (*FlagName* *|* [*ILFlag*](lowlevelil.md#binaryninja.lowlevelil.ILFlag
            "binaryninja.lowlevelil.ILFlag") *|* *FlagIndex*) –

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")

    get_var_for_reg(*reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_var_for_reg)
    :   Parameters:
        :   **reg** (*RegisterName* *|*
            [*ILRegister*](lowlevelil.md#binaryninja.lowlevelil.ILRegister
            "binaryninja.lowlevelil.ILRegister") *|* *RegisterIndex*) –

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")

    get_var_for_reg_after(*reg: RegisterName | [ILRegister](lowlevelil.md#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | RegisterIndex*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_var_for_reg_after)
    :   Parameters:
        :   **reg** (*RegisterName* *|*
            [*ILRegister*](lowlevelil.md#binaryninja.lowlevelil.ILRegister
            "binaryninja.lowlevelil.ILRegister") *|* *RegisterIndex*) –

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")

    get_var_for_stack_location(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_var_for_stack_location)
    :   Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")

    get_var_for_stack_location_after(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.get_var_for_stack_location_after)
    :   Parameters:
        :   **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*Variable*](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")

    *static* show_mlil_hierarchy()[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.show_mlil_hierarchy)
    :   Opens a new tab showing the MLIL hierarchy which includes classes which can easily be
        used with isinstance to match multiple types of IL instructions.

    traverse(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, **args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, ***kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.traverse)
    :   `traverse` is a generator that allows you to traverse the MediumLevelILInstruction in a
        depth-first manner. It will yield the result of the callback function for each node in
        the tree. Arguments can be passed to the callback function using `args` and `kwargs`.
        See the [Developer Docs](https://docs.binary.ninja/dev/concepts.html#walking-ils) for
        more examples.

        Parameters:
        :   - **cb** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in
              Python
              v3.14)")*[**[*[*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction")*,*
              [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
              v3.14)")*]**,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")*]*) – The callback function to call for each node in the
              MediumLevelILInstruction
            - **args** (*Any*) – Custom user-defined arguments
            - **kwargs** (*Any*) – Custom user-defined keyword arguments
            - **cb** –

        Returns:
        :   An iterator of the results of the callback function

        Return type:
        :   *Iterator*[*Any*]

        Example:
        :   ```
            >>> def get_constant_less_than_value(inst: MediumLevelILInstruction, value: int) -> int:
            >>>     if isinstance(inst, Constant) and inst.constant < value:
            >>>         return inst.constant
            >>>
            >>> list(inst.traverse(get_constant_less_than_value, 10))
            ```

    visit(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'root'*, *parent: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.visit)
    :   Visits all MediumLevelILInstructions in the operands of this instruction and any
        sub-instructions. In the callback you provide, you likely only need to interact with the
        second argument (see the example below).

        Parameters:
        :   - **cb** (*MediumLevelILVisitorCallback*) – Callback function that takes the name of the
              operand, the operand, operand type, and parent instruction
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **parent**
              ([*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction") *|* *None*) –

        Returns:
        :   True if all instructions were visited, False if the callback returned False

        Example:
        :   ```
            >>> def visitor(_a, inst, _c, _d) -> bool:
            >>>     if isinstance(inst, Constant):
            >>>         print(f"Found constant: {inst.constant}")
            >>>         return False # Stop recursion (once we find a constant, don't recurse in to any sub-instructions (which there won't actually be any...))
            >>>     # Otherwise, keep recursing the subexpressions of this instruction; if no return value is provided, it'll keep descending
            >>>
            >>> # Finds all constants used in the program
            >>> for inst in current_mlil.instructions:
            >>>     inst.visit(visitor)
            ```

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`MediumLevelILInstruction.traverse`](#binaryninja.mediumlevelil.MediumLevelILInstruction.traverse
        "binaryninja.mediumlevelil.MediumLevelILInstruction.traverse") instead.

    visit_all(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'root'*, *parent: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.visit_all)
    :   Visits all operands of this instruction and all operands of any sub-instructions. Using
        pre-order traversal.

        Parameters:
        :   - **cb** (*MediumLevelILVisitorCallback*) – Callback function that takes the name of the
              operand, the operand, operand type, and parent instruction
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **parent**
              ([*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction") *|* *None*) –

        Returns:
        :   True if all instructions were visited, False if the callback returned False

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`MediumLevelILInstruction.traverse`](#binaryninja.mediumlevelil.MediumLevelILInstruction.traverse
        "binaryninja.mediumlevelil.MediumLevelILInstruction.traverse") instead.

    visit_operands(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'root'*, *parent: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILInstruction.visit_operands)
    :   Visits all leaf operands of this instruction and any sub-instructions.

        Parameters:
        :   - **cb** (*MediumLevelILVisitorCallback*) – Callback function that takes the name of the
              operand, the operand, operand type, and parent instruction
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **parent**
              ([*MediumLevelILInstruction*](#binaryninja.mediumlevelil.MediumLevelILInstruction
              "binaryninja.mediumlevelil.MediumLevelILInstruction") *|* *None*) –

        Returns:
        :   True if all instructions were visited, False if the callback returned False

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`MediumLevelILInstruction.traverse`](#binaryninja.mediumlevelil.MediumLevelILInstruction.traverse
        "binaryninja.mediumlevelil.MediumLevelILInstruction.traverse") instead.

    ILOperations*: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar "(in Python v3.14)")[[Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[MediumLevelILOperation](enums.md#binaryninja.enums.MediumLevelILOperation "binaryninja.enums.MediumLevelILOperation"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]]]* *= {MediumLevelILOperation.MLIL_NOP: [], MediumLevelILOperation.MLIL_SET_VAR: [('dest', 'var'), ('src', 'expr')], MediumLevelILOperation.MLIL_SET_VAR_FIELD: [('dest', 'var'), ('offset', 'int'), ('src', 'expr')], MediumLevelILOperation.MLIL_SET_VAR_SPLIT: [('high', 'var'), ('low', 'var'), ('src', 'expr')], MediumLevelILOperation.MLIL_LOAD: [('src', 'expr')], MediumLevelILOperation.MLIL_LOAD_STRUCT: [('src', 'expr'), ('offset', 'int')], MediumLevelILOperation.MLIL_STORE: [('dest', 'expr'), ('src', 'expr')], MediumLevelILOperation.MLIL_STORE_STRUCT: [('dest', 'expr'), ('offset', 'int'), ('src', 'expr')], MediumLevelILOperation.MLIL_VAR: [('src', 'var')], MediumLevelILOperation.MLIL_VAR_FIELD: [('src', 'var'), ('offset', 'int')], MediumLevelILOperation.MLIL_VAR_SPLIT: [('high', 'var'), ('low', 'var')], MediumLevelILOperation.MLIL_ADDRESS_OF: [('src', 'var')], MediumLevelILOperation.MLIL_ADDRESS_OF_FIELD: [('src', 'var'), ('offset', 'int')], MediumLevelILOperation.MLIL_CONST: [('constant', 'int')], MediumLevelILOperation.MLIL_CONST_DATA: [('constant', 'ConstantData')], MediumLevelILOperation.MLIL_CONST_PTR: [('constant', 'int')], MediumLevelILOperation.MLIL_EXTERN_PTR: [('constant', 'int'), ('offset', 'int')], MediumLevelILOperation.MLIL_FLOAT_CONST: [('constant', 'float')], MediumLevelILOperation.MLIL_IMPORT: [('constant', 'int')], MediumLevelILOperation.MLIL_ADD: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_ADC: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], MediumLevelILOperation.MLIL_SUB: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_SBB: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], MediumLevelILOperation.MLIL_AND: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_OR: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_XOR: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_LSL: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_LSR: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_ASR: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_ROL: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_RLC: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], MediumLevelILOperation.MLIL_ROR: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_RRC: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], MediumLevelILOperation.MLIL_MUL: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_MULU_DP: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_MULS_DP: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_DIVU: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_DIVU_DP: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_DIVS: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_DIVS_DP: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_MODU: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_MODU_DP: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_MODS: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_MODS_DP: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_NEG: [('src', 'expr')], MediumLevelILOperation.MLIL_NOT: [('src', 'expr')], MediumLevelILOperation.MLIL_SX: [('src', 'expr')], MediumLevelILOperation.MLIL_ZX: [('src', 'expr')], MediumLevelILOperation.MLIL_LOW_PART: [('src', 'expr')], MediumLevelILOperation.MLIL_JUMP: [('dest', 'expr')], MediumLevelILOperation.MLIL_JUMP_TO: [('dest', 'expr'), ('targets', 'target_map')], MediumLevelILOperation.MLIL_RET_HINT: [('dest', 'expr')], MediumLevelILOperation.MLIL_CALL: [('output', 'var_list'), ('dest', 'expr'), ('params', 'expr_list')], MediumLevelILOperation.MLIL_CALL_UNTYPED: [('output', 'expr'), ('dest', 'expr'), ('params', 'expr'), ('stack', 'expr')], MediumLevelILOperation.MLIL_CALL_OUTPUT: [('dest', 'var_list')], MediumLevelILOperation.MLIL_CALL_PARAM: [('src', 'expr_list')], MediumLevelILOperation.MLIL_SEPARATE_PARAM_LIST: [('params', 'expr_list')], MediumLevelILOperation.MLIL_SHARED_PARAM_SLOT: [('params', 'expr_list')], MediumLevelILOperation.MLIL_RET: [('src', 'expr_list')], MediumLevelILOperation.MLIL_NORET: [], MediumLevelILOperation.MLIL_IF: [('condition', 'expr'), ('true', 'int'), ('false', 'int')], MediumLevelILOperation.MLIL_GOTO: [('dest', 'int')], MediumLevelILOperation.MLIL_CMP_E: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_CMP_NE: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_CMP_SLT: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_CMP_ULT: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_CMP_SLE: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_CMP_ULE: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_CMP_SGE: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_CMP_UGE: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_CMP_SGT: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_CMP_UGT: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_TEST_BIT: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_BOOL_TO_INT: [('src', 'expr')], MediumLevelILOperation.MLIL_ADD_OVERFLOW: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_SYSCALL: [('output', 'var_list'), ('params', 'expr_list')], MediumLevelILOperation.MLIL_SYSCALL_UNTYPED: [('output', 'expr'), ('params', 'expr'), ('stack', 'expr')], MediumLevelILOperation.MLIL_TAILCALL: [('output', 'var_list'), ('dest', 'expr'), ('params', 'expr_list')], MediumLevelILOperation.MLIL_TAILCALL_UNTYPED: [('output', 'expr'), ('dest', 'expr'), ('params', 'expr'), ('stack', 'expr')], MediumLevelILOperation.MLIL_INTRINSIC: [('output', 'var_list'), ('intrinsic', 'intrinsic'), ('params', 'expr_list')], MediumLevelILOperation.MLIL_FREE_VAR_SLOT: [('dest', 'var')], MediumLevelILOperation.MLIL_BP: [], MediumLevelILOperation.MLIL_TRAP: [('vector', 'int')], MediumLevelILOperation.MLIL_UNDEF: [], MediumLevelILOperation.MLIL_UNIMPL: [], MediumLevelILOperation.MLIL_UNIMPL_MEM: [('src', 'expr')], MediumLevelILOperation.MLIL_FADD: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FSUB: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FMUL: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FDIV: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FSQRT: [('src', 'expr')], MediumLevelILOperation.MLIL_FNEG: [('src', 'expr')], MediumLevelILOperation.MLIL_FABS: [('src', 'expr')], MediumLevelILOperation.MLIL_FLOAT_TO_INT: [('src', 'expr')], MediumLevelILOperation.MLIL_INT_TO_FLOAT: [('src', 'expr')], MediumLevelILOperation.MLIL_FLOAT_CONV: [('src', 'expr')], MediumLevelILOperation.MLIL_ROUND_TO_INT: [('src', 'expr')], MediumLevelILOperation.MLIL_FLOOR: [('src', 'expr')], MediumLevelILOperation.MLIL_CEIL: [('src', 'expr')], MediumLevelILOperation.MLIL_FTRUNC: [('src', 'expr')], MediumLevelILOperation.MLIL_FCMP_E: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FCMP_NE: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FCMP_LT: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FCMP_LE: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FCMP_GE: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FCMP_GT: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FCMP_O: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_FCMP_UO: [('left', 'expr'), ('right', 'expr')], MediumLevelILOperation.MLIL_SET_VAR_SSA: [('dest', 'var_ssa'), ('src', 'expr')], MediumLevelILOperation.MLIL_SET_VAR_SSA_FIELD: [('dest', 'var_ssa_dest_and_src'), ('prev', 'var_ssa_dest_and_src'), ('offset', 'int'), ('src', 'expr')], MediumLevelILOperation.MLIL_SET_VAR_SPLIT_SSA: [('high', 'var_ssa'), ('low', 'var_ssa'), ('src', 'expr')], MediumLevelILOperation.MLIL_SET_VAR_ALIASED: [('dest', 'var_ssa_dest_and_src'), ('prev', 'var_ssa_dest_and_src'), ('src', 'expr')], MediumLevelILOperation.MLIL_SET_VAR_ALIASED_FIELD: [('dest', 'var_ssa_dest_and_src'), ('prev', 'var_ssa_dest_and_src'), ('offset', 'int'), ('src', 'expr')], MediumLevelILOperation.MLIL_VAR_SSA: [('src', 'var_ssa')], MediumLevelILOperation.MLIL_VAR_SSA_FIELD: [('src', 'var_ssa'), ('offset', 'int')], MediumLevelILOperation.MLIL_VAR_ALIASED: [('src', 'var_ssa')], MediumLevelILOperation.MLIL_VAR_ALIASED_FIELD: [('src', 'var_ssa'), ('offset', 'int')], MediumLevelILOperation.MLIL_VAR_SPLIT_SSA: [('high', 'var_ssa'), ('low', 'var_ssa')], MediumLevelILOperation.MLIL_CALL_SSA: [('output', 'expr'), ('output_dest_memory', 'int'), ('dest', 'expr'), ('params', 'expr_list'), ('src_memory', 'int')], MediumLevelILOperation.MLIL_CALL_UNTYPED_SSA: [('output', 'expr'), ('dest', 'expr'), ('params', 'expr'), ('stack', 'expr')], MediumLevelILOperation.MLIL_SYSCALL_SSA: [('output', 'expr'), ('params', 'expr_list'), ('src_memory', 'int')], MediumLevelILOperation.MLIL_SYSCALL_UNTYPED_SSA: [('output', 'expr'), ('params', 'expr'), ('stack', 'expr')], MediumLevelILOperation.MLIL_TAILCALL_SSA: [('output', 'expr'), ('output_dest_memory', 'int'), ('dest', 'expr'), ('params', 'expr_list'), ('src_memory', 'int')], MediumLevelILOperation.MLIL_TAILCALL_UNTYPED_SSA: [('output', 'expr'), ('dest', 'expr'), ('params', 'expr'), ('stack', 'expr')], MediumLevelILOperation.MLIL_CALL_PARAM_SSA: [('src_memory', 'int'), ('src', 'expr_list')], MediumLevelILOperation.MLIL_CALL_OUTPUT_SSA: [('dest_memory', 'int'), ('dest', 'var_ssa_list')], MediumLevelILOperation.MLIL_MEMORY_INTRINSIC_OUTPUT_SSA: [('dest_memory', 'int'), ('output', 'var_ssa_list')], MediumLevelILOperation.MLIL_LOAD_SSA: [('src', 'expr'), ('src_memory', 'int')], MediumLevelILOperation.MLIL_LOAD_STRUCT_SSA: [('src', 'expr'), ('offset', 'int'), ('src_memory', 'int')], MediumLevelILOperation.MLIL_STORE_SSA: [('dest', 'expr'), ('dest_memory', 'int'), ('src_memory', 'int'), ('src', 'expr')], MediumLevelILOperation.MLIL_STORE_STRUCT_SSA: [('dest', 'expr'), ('offset', 'int'), ('dest_memory', 'int'), ('src_memory', 'int'), ('src', 'expr')], MediumLevelILOperation.MLIL_INTRINSIC_SSA: [('output', 'var_ssa_list'), ('intrinsic', 'intrinsic'), ('params', 'expr_list')], MediumLevelILOperation.MLIL_MEMORY_INTRINSIC_SSA: [('output', 'expr'), ('intrinsic', 'intrinsic'), ('params', 'expr_list'), ('src_memory', 'int')], MediumLevelILOperation.MLIL_FREE_VAR_SLOT_SSA: [('prev', 'var_ssa_dest_and_src')], MediumLevelILOperation.MLIL_VAR_PHI: [('dest', 'var_ssa'), ('src', 'var_ssa_list')], MediumLevelILOperation.MLIL_MEM_PHI: [('dest_memory', 'int'), ('src_memory', 'int_list')]}*

    *property* address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* attributes*: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ILInstructionAttribute](enums.md#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute")]*
    :   The set of optional attributes placed on the instruction

    *property* branch_dependence*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [ILBranchDependence](enums.md#binaryninja.enums.ILBranchDependence "binaryninja.enums.ILBranchDependence")]*
    :   Set of branching instructions that must take the true or false path to reach this
        instruction

    *property* core_operands*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    *property* expr_type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Type of expression

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    *property* high_level_il*: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   High level IL form of this expression

    *property* hlil*: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Alias for high_level_il

    *property* hlils*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    *property* il_basic_block*: [MediumLevelILBasicBlock](#binaryninja.mediumlevelil.MediumLevelILBasicBlock "binaryninja.mediumlevelil.MediumLevelILBasicBlock")*
    :   IL basic block object containing this expression (read-only) (only available on
        finalized functions)

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* instruction_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* llil*: [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Alias for low_level_il

    *property* llils*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

    *property* low_level_il*: [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Low level IL form of this expression

    *property* non_ssa_form*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*
    :   Non-SSA form of expression (read-only)

    *property* operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData")]*
    :   Operands for the instruction

        Consider using more specific APIs for `src`, `dest`, `params`, etc where appropriate.

    *property* operation*: [MediumLevelILOperation](enums.md#binaryninja.enums.MediumLevelILOperation "binaryninja.enums.MediumLevelILOperation")*

    *property* possible_values*: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*
    :   Possible values of expression using path-sensitive static data flow analysis (read-only)

    *property* postfix_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData")]*
    :   All operands in the expression tree in postfix order

    *property* prefix_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData")]*
    :   All operands in the expression tree in prefix order

    *property* raw_operands*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*
    :   Raw operand expression indices as specified by the core structure (read-only)

    *property* size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* source_location*: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation")*

    *property* source_operand*: ExpressionIndex*

    *property* ssa_form*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*
    :   SSA form of expression (read-only)

    *property* ssa_memory_version*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Version of active memory contents in SSA form for this instruction

    *property* ssa_memory_version_after*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Version of active memory contents in SSA form after this instruction

    *property* tokens*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*
    :   MLIL tokens (read-only)

    *property* value*: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*
    :   Value of expression if constant or a known value (read-only)

    *property* vars_address_taken*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   Non-unique list of variables whose address is taken by instruction

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables written by instruction

## MediumLevelILIntToFloat

*class* MediumLevelILIntToFloat[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILIntToFloat)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILIntToFloat(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILIntrinsic

*class* MediumLevelILIntrinsic[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILIntrinsic)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Intrinsic`](commonil.md#binaryninja.commonil.Intrinsic
    "binaryninja.commonil.Intrinsic")

    MediumLevelILIntrinsic(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* intrinsic*: [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables written by instruction

## MediumLevelILIntrinsicSsa

*class* MediumLevelILIntrinsicSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILIntrinsicSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILIntrinsicSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* intrinsic*: [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables written by instruction

## MediumLevelILJump

*class* MediumLevelILJump[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILJump)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    MediumLevelILJump(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILJumpTo

*class* MediumLevelILJumpTo[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILJumpTo)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    MediumLevelILJumpTo(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* targets*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

## MediumLevelILLabel

*class* MediumLevelILLabel[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILLabel)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle: BNMediumLevelILLabel | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILLabel.__init__)
    :   Parameters:
        :   **handle** (*BNMediumLevelILLabel* *|* *None*) –

    *property* operand*: InstructionIndex*

    *property* ref*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* resolved*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

## MediumLevelILLoad

*class* MediumLevelILLoad[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILLoad)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Load`](commonil.md#binaryninja.commonil.Load "binaryninja.commonil.Load")

    MediumLevelILLoad(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILLoadSsa

*class* MediumLevelILLoadSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILLoadSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Load`](commonil.md#binaryninja.commonil.Load "binaryninja.commonil.Load"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILLoadSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILLoadStruct

*class* MediumLevelILLoadStruct[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILLoadStruct)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Load`](commonil.md#binaryninja.commonil.Load "binaryninja.commonil.Load")

    MediumLevelILLoadStruct(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILLoadStructSsa

*class* MediumLevelILLoadStructSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILLoadStructSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Load`](commonil.md#binaryninja.commonil.Load "binaryninja.commonil.Load"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILLoadStructSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILLowPart

*class* MediumLevelILLowPart[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILLowPart)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILLowPart(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILLsl

*class* MediumLevelILLsl[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILLsl)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILLsl(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILLsr

*class* MediumLevelILLsr[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILLsr)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILLsr(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILMemPhi

*class* MediumLevelILMemPhi[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILMemPhi)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Memory`](commonil.md#binaryninja.commonil.Memory "binaryninja.commonil.Memory"),
    [`Phi`](commonil.md#binaryninja.commonil.Phi "binaryninja.commonil.Phi")

    MediumLevelILMemPhi(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src_memory*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

## MediumLevelILMemoryIntrinsicOutputSsa

*class* MediumLevelILMemoryIntrinsicOutputSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILMemoryIntrinsicOutputSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILMemoryIntrinsicOutputSsa(function: ‘MediumLevelILFunction’, expr_index:
    <function NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

## MediumLevelILMemoryIntrinsicSsa

*class* MediumLevelILMemoryIntrinsicSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILMemoryIntrinsicSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILMemoryIntrinsicSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* intrinsic*: [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILMods

*class* MediumLevelILMods[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILMods)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"), [`Signed`](commonil.md#binaryninja.commonil.Signed
    "binaryninja.commonil.Signed")

    MediumLevelILMods(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILModsDp

*class* MediumLevelILModsDp[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILModsDp)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    MediumLevelILModsDp(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILModu

*class* MediumLevelILModu[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILModu)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILModu(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILModuDp

*class* MediumLevelILModuDp[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILModuDp)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    MediumLevelILModuDp(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILMul

*class* MediumLevelILMul[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILMul)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILMul(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILMulsDp

*class* MediumLevelILMulsDp[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILMulsDp)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    MediumLevelILMulsDp(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILMuluDp

*class* MediumLevelILMuluDp[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILMuluDp)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    MediumLevelILMuluDp(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILNeg

*class* MediumLevelILNeg[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILNeg)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILNeg(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILNop

*class* MediumLevelILNop[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILNop)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILNop(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILNoret

*class* MediumLevelILNoret[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILNoret)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    MediumLevelILNoret(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILNot

*class* MediumLevelILNot[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILNot)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILNot(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILOperationAndSize

*class* MediumLevelILOperationAndSize[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILOperationAndSize)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    MediumLevelILOperationAndSize(operation: binaryninja.enums.MediumLevelILOperation, size:
    int)

    __init__(*operation: [MediumLevelILOperation](enums.md#binaryninja.enums.MediumLevelILOperation "binaryninja.enums.MediumLevelILOperation")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **operation**
              ([*MediumLevelILOperation*](enums.md#binaryninja.enums.MediumLevelILOperation
              "binaryninja.enums.MediumLevelILOperation")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    operation*: [MediumLevelILOperation](enums.md#binaryninja.enums.MediumLevelILOperation "binaryninja.enums.MediumLevelILOperation")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILOr

*class* MediumLevelILOr[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILOr)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILOr(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILRet

*class* MediumLevelILRet[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILRet)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Return`](commonil.md#binaryninja.commonil.Return "binaryninja.commonil.Return")

    MediumLevelILRet(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

## MediumLevelILRetHint

*class* MediumLevelILRetHint[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILRetHint)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`ControlFlow`](commonil.md#binaryninja.commonil.ControlFlow
    "binaryninja.commonil.ControlFlow")

    MediumLevelILRetHint(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILRlc

*class* MediumLevelILRlc[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILRlc)
:   Bases: [`MediumLevelILCarryBase`](#binaryninja.mediumlevelil.MediumLevelILCarryBase
    "binaryninja.mediumlevelil.MediumLevelILCarryBase")

    MediumLevelILRlc(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILRol

*class* MediumLevelILRol[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILRol)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILRol(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILRor

*class* MediumLevelILRor[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILRor)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILRor(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILRoundToInt

*class* MediumLevelILRoundToInt[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILRoundToInt)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    MediumLevelILRoundToInt(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILRrc

*class* MediumLevelILRrc[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILRrc)
:   Bases: [`MediumLevelILCarryBase`](#binaryninja.mediumlevelil.MediumLevelILCarryBase
    "binaryninja.mediumlevelil.MediumLevelILCarryBase")

    MediumLevelILRrc(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILSbb

*class* MediumLevelILSbb[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSbb)
:   Bases: [`MediumLevelILCarryBase`](#binaryninja.mediumlevelil.MediumLevelILCarryBase
    "binaryninja.mediumlevelil.MediumLevelILCarryBase")

    MediumLevelILSbb(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILSeparateParamList

*class* MediumLevelILSeparateParamList[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSeparateParamList)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILSeparateParamList(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

## MediumLevelILSetVar

*class* MediumLevelILSetVar[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSetVar)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar")

    MediumLevelILSetVar(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables written by instruction

## MediumLevelILSetVarAliased

*class* MediumLevelILSetVarAliased[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSetVarAliased)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILSetVarAliased(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* prev*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables written by instruction

## MediumLevelILSetVarAliasedField

*class* MediumLevelILSetVarAliasedField[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSetVarAliasedField)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILSetVarAliasedField(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* prev*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

## MediumLevelILSetVarField

*class* MediumLevelILSetVarField[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSetVarField)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar")

    MediumLevelILSetVarField(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILSetVarSplit

*class* MediumLevelILSetVarSplit[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSetVarSplit)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar")

    MediumLevelILSetVarSplit(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    *property* high*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* low*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables written by instruction

## MediumLevelILSetVarSplitSsa

*class* MediumLevelILSetVarSplitSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSetVarSplitSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILSetVarSplitSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    *property* high*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* low*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables written by instruction

## MediumLevelILSetVarSsa

*class* MediumLevelILSetVarSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSetVarSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILSetVarSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables written by instruction

## MediumLevelILSetVarSsaField

*class* MediumLevelILSetVarSsaField[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSetVarSsaField)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILSetVarSsaField(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* prev*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables written by instruction

## MediumLevelILSharedParamSlot

*class* MediumLevelILSharedParamSlot[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSharedParamSlot)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILSharedParamSlot(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

## MediumLevelILStore

*class* MediumLevelILStore[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILStore)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Store`](commonil.md#binaryninja.commonil.Store "binaryninja.commonil.Store")

    MediumLevelILStore(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILStoreSsa

*class* MediumLevelILStoreSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILStoreSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Store`](commonil.md#binaryninja.commonil.Store "binaryninja.commonil.Store"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILStoreSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILStoreStruct

*class* MediumLevelILStoreStruct[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILStoreStruct)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Store`](commonil.md#binaryninja.commonil.Store "binaryninja.commonil.Store")

    MediumLevelILStoreStruct(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILStoreStructSsa

*class* MediumLevelILStoreStructSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILStoreStructSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Store`](commonil.md#binaryninja.commonil.Store "binaryninja.commonil.Store"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILStoreStructSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILSub

*class* MediumLevelILSub[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSub)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILSub(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILSx

*class* MediumLevelILSx[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSx)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILSx(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILSyscall

*class* MediumLevelILSyscall[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSyscall)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Syscall`](commonil.md#binaryninja.commonil.Syscall "binaryninja.commonil.Syscall")

    MediumLevelILSyscall(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

## MediumLevelILSyscallSsa

*class* MediumLevelILSyscallSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSyscallSsa)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Syscall`](commonil.md#binaryninja.commonil.Syscall "binaryninja.commonil.Syscall"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILSyscallSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* output_dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILSyscallUntyped

*class* MediumLevelILSyscallUntyped[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSyscallUntyped)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Syscall`](commonil.md#binaryninja.commonil.Syscall "binaryninja.commonil.Syscall")

    MediumLevelILSyscallUntyped(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* stack*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILSyscallUntypedSsa

*class* MediumLevelILSyscallUntypedSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILSyscallUntypedSsa)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Syscall`](commonil.md#binaryninja.commonil.Syscall "binaryninja.commonil.Syscall"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILSyscallUntypedSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* output_dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* params_src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* stack*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILTailcall

*class* MediumLevelILTailcall[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILTailcall)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Tailcall`](commonil.md#binaryninja.commonil.Tailcall "binaryninja.commonil.Tailcall")

    MediumLevelILTailcall(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

## MediumLevelILTailcallSsa

*class* MediumLevelILTailcallSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILTailcallSsa)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Tailcall`](commonil.md#binaryninja.commonil.Tailcall "binaryninja.commonil.Tailcall"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILTailcallSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* output_dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILTailcallUntyped

*class* MediumLevelILTailcallUntyped[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILTailcallUntyped)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Tailcall`](commonil.md#binaryninja.commonil.Tailcall "binaryninja.commonil.Tailcall")

    MediumLevelILTailcallUntyped(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* stack*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILTailcallUntypedSsa

*class* MediumLevelILTailcallUntypedSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILTailcallUntypedSsa)
:   Bases: [`MediumLevelILCallBase`](#binaryninja.mediumlevelil.MediumLevelILCallBase
    "binaryninja.mediumlevelil.MediumLevelILCallBase"),
    [`Tailcall`](commonil.md#binaryninja.commonil.Tailcall "binaryninja.commonil.Tailcall"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILTailcallUntypedSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* output_dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* stack*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILTestBit

*class* MediumLevelILTestBit[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILTestBit)
:   Bases:
    [`MediumLevelILComparisonBase`](#binaryninja.mediumlevelil.MediumLevelILComparisonBase
    "binaryninja.mediumlevelil.MediumLevelILComparisonBase")

    MediumLevelILTestBit(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILTrap

*class* MediumLevelILTrap[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILTrap)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    MediumLevelILTrap(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* vector*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## MediumLevelILUnaryBase

*class* MediumLevelILUnaryBase[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILUnaryBase)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`UnaryOperation`](commonil.md#binaryninja.commonil.UnaryOperation
    "binaryninja.commonil.UnaryOperation")

    MediumLevelILUnaryBase(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILUndef

*class* MediumLevelILUndef[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILUndef)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILUndef(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILUnimpl

*class* MediumLevelILUnimpl[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILUnimpl)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILUnimpl(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILUnimplMem

*class* MediumLevelILUnimplMem[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILUnimplMem)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`Memory`](commonil.md#binaryninja.commonil.Memory "binaryninja.commonil.Memory")

    MediumLevelILUnimplMem(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")*

## MediumLevelILVar

*class* MediumLevelILVar[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILVar)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`VariableInstruction`](commonil.md#binaryninja.commonil.VariableInstruction
    "binaryninja.commonil.VariableInstruction")

    MediumLevelILVar(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    *property* var*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## MediumLevelILVarAliased

*class* MediumLevelILVarAliased[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILVarAliased)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA"),
    [`AliasedVariableInstruction`](commonil.md#binaryninja.commonil.AliasedVariableInstruction
    "binaryninja.commonil.AliasedVariableInstruction")

    MediumLevelILVarAliased(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## MediumLevelILVarAliasedField

*class* MediumLevelILVarAliasedField[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILVarAliasedField)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILVarAliasedField(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## MediumLevelILVarField

*class* MediumLevelILVarField[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILVarField)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILVarField(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## MediumLevelILVarPhi

*class* MediumLevelILVarPhi[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILVarPhi)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar"),
    [`Phi`](commonil.md#binaryninja.commonil.Phi "binaryninja.commonil.Phi"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILVarPhi(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* dest*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables read by instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   List of variables written by instruction

## MediumLevelILVarSplit

*class* MediumLevelILVarSplit[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILVarSplit)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction")

    MediumLevelILVarSplit(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    *property* high*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* low*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## MediumLevelILVarSplitSsa

*class* MediumLevelILVarSplitSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILVarSplitSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILVarSplitSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    *property* high*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* low*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## MediumLevelILVarSsa

*class* MediumLevelILVarSsa[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILVarSsa)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSAVariableInstruction`](commonil.md#binaryninja.commonil.SSAVariableInstruction
    "binaryninja.commonil.SSAVariableInstruction")

    MediumLevelILVarSsa(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* var*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## MediumLevelILVarSsaField

*class* MediumLevelILVarSsaField[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILVarSsaField)
:   Bases: [`MediumLevelILInstruction`](#binaryninja.mediumlevelil.MediumLevelILInstruction
    "binaryninja.mediumlevelil.MediumLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    MediumLevelILVarSsaField(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [MediumLevelILOperationAndSize](#binaryninja.mediumlevelil.MediumLevelILOperationAndSize "binaryninja.mediumlevelil.MediumLevelILOperationAndSize") | [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [SSAVariable](#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## MediumLevelILXor

*class* MediumLevelILXor[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILXor)
:   Bases: [`MediumLevelILBinaryBase`](#binaryninja.mediumlevelil.MediumLevelILBinaryBase
    "binaryninja.mediumlevelil.MediumLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILXor(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## MediumLevelILZx

*class* MediumLevelILZx[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#MediumLevelILZx)
:   Bases: [`MediumLevelILUnaryBase`](#binaryninja.mediumlevelil.MediumLevelILUnaryBase
    "binaryninja.mediumlevelil.MediumLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    MediumLevelILZx(function: ‘MediumLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x1077f7670>, instr:
    binaryninja.mediumlevelil.CoreMediumLevelILInstruction, instr_index: <function
    NewType.<locals>.new_type at 0x105107a60>)

    __init__(*function: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*MediumLevelILFunction*](#binaryninja.mediumlevelil.MediumLevelILFunction
              "binaryninja.mediumlevelil.MediumLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreMediumLevelILInstruction*](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction
              "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [MediumLevelILFunction](#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    instr*: [CoreMediumLevelILInstruction](#binaryninja.mediumlevelil.CoreMediumLevelILInstruction "binaryninja.mediumlevelil.CoreMediumLevelILInstruction")*

    instr_index*: InstructionIndex*

## SSAVariable

*class* SSAVariable[[source]](https://api.binary.ninja/_modules/binaryninja/mediumlevelil.html#SSAVariable)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    SSAVariable(var: ‘variable.Variable’, version: int)

    __init__(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) –
            - **version** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    *property* dead_store_elimination*: [DeadStoreElimination](enums.md#binaryninja.enums.DeadStoreElimination "binaryninja.enums.DeadStoreElimination")*
    :   returns the dead store elimination setting for this variable (read-only)

    *property* def_site*: [MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Gets the IL instructions where this SSAVariable is defined.

    *property* function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*
    :   returns the source Function object which this variable belongs to

    *property* il_function*: function.ILFunctionType*
    :   returns the il Function object which this variable belongs to

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type")*

    *property* use_sites*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*
    :   Gets the list of IL instructions where this SSAVariable is used inside of this function.

    var*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    version*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
