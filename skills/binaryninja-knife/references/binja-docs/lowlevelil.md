# lowlevelil module

| Class | Description |
| --- | --- |
| [`binaryninja.lowlevelil.CoreLowLevelILInstruction`](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction") |  |
| [`binaryninja.lowlevelil.ILFlag`](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") |  |
| [`binaryninja.lowlevelil.ILIntrinsic`](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") |  |
| [`binaryninja.lowlevelil.ILRegister`](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") |  |
| [`binaryninja.lowlevelil.ILRegisterStack`](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") |  |
| [`binaryninja.lowlevelil.ILSemanticFlagClass`](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") |  |
| [`binaryninja.lowlevelil.ILSemanticFlagGroup`](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") |  |
| [`binaryninja.lowlevelil.LowLevelILAdc`](#binaryninja.lowlevelil.LowLevelILAdc "binaryninja.lowlevelil.LowLevelILAdc") |  |
| [`binaryninja.lowlevelil.LowLevelILAdd`](#binaryninja.lowlevelil.LowLevelILAdd "binaryninja.lowlevelil.LowLevelILAdd") |  |
| [`binaryninja.lowlevelil.LowLevelILAddOverflow`](#binaryninja.lowlevelil.LowLevelILAddOverflow "binaryninja.lowlevelil.LowLevelILAddOverflow") |  |
| [`binaryninja.lowlevelil.LowLevelILAnd`](#binaryninja.lowlevelil.LowLevelILAnd "binaryninja.lowlevelil.LowLevelILAnd") |  |
| [`binaryninja.lowlevelil.LowLevelILAsr`](#binaryninja.lowlevelil.LowLevelILAsr "binaryninja.lowlevelil.LowLevelILAsr") |  |
| [`binaryninja.lowlevelil.LowLevelILAssert`](#binaryninja.lowlevelil.LowLevelILAssert "binaryninja.lowlevelil.LowLevelILAssert") |  |
| [`binaryninja.lowlevelil.LowLevelILAssertSsa`](#binaryninja.lowlevelil.LowLevelILAssertSsa "binaryninja.lowlevelil.LowLevelILAssertSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILBasicBlock`](#binaryninja.lowlevelil.LowLevelILBasicBlock "binaryninja.lowlevelil.LowLevelILBasicBlock") | The `LogLevelILBasicBlock` object is returned during analysis and should not be directly… |
| [`binaryninja.lowlevelil.LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase "binaryninja.lowlevelil.LowLevelILBinaryBase") |  |
| [`binaryninja.lowlevelil.LowLevelILBoolToInt`](#binaryninja.lowlevelil.LowLevelILBoolToInt "binaryninja.lowlevelil.LowLevelILBoolToInt") |  |
| [`binaryninja.lowlevelil.LowLevelILBp`](#binaryninja.lowlevelil.LowLevelILBp "binaryninja.lowlevelil.LowLevelILBp") |  |
| [`binaryninja.lowlevelil.LowLevelILCall`](#binaryninja.lowlevelil.LowLevelILCall "binaryninja.lowlevelil.LowLevelILCall") |  |
| [`binaryninja.lowlevelil.LowLevelILCallOutputSsa`](#binaryninja.lowlevelil.LowLevelILCallOutputSsa "binaryninja.lowlevelil.LowLevelILCallOutputSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILCallParam`](#binaryninja.lowlevelil.LowLevelILCallParam "binaryninja.lowlevelil.LowLevelILCallParam") |  |
| [`binaryninja.lowlevelil.LowLevelILCallSsa`](#binaryninja.lowlevelil.LowLevelILCallSsa "binaryninja.lowlevelil.LowLevelILCallSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILCallStackAdjust`](#binaryninja.lowlevelil.LowLevelILCallStackAdjust "binaryninja.lowlevelil.LowLevelILCallStackAdjust") |  |
| [`binaryninja.lowlevelil.LowLevelILCallStackSsa`](#binaryninja.lowlevelil.LowLevelILCallStackSsa "binaryninja.lowlevelil.LowLevelILCallStackSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILCarryBase`](#binaryninja.lowlevelil.LowLevelILCarryBase "binaryninja.lowlevelil.LowLevelILCarryBase") |  |
| [`binaryninja.lowlevelil.LowLevelILCeil`](#binaryninja.lowlevelil.LowLevelILCeil "binaryninja.lowlevelil.LowLevelILCeil") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpE`](#binaryninja.lowlevelil.LowLevelILCmpE "binaryninja.lowlevelil.LowLevelILCmpE") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpNe`](#binaryninja.lowlevelil.LowLevelILCmpNe "binaryninja.lowlevelil.LowLevelILCmpNe") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpSge`](#binaryninja.lowlevelil.LowLevelILCmpSge "binaryninja.lowlevelil.LowLevelILCmpSge") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpSgt`](#binaryninja.lowlevelil.LowLevelILCmpSgt "binaryninja.lowlevelil.LowLevelILCmpSgt") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpSle`](#binaryninja.lowlevelil.LowLevelILCmpSle "binaryninja.lowlevelil.LowLevelILCmpSle") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpSlt`](#binaryninja.lowlevelil.LowLevelILCmpSlt "binaryninja.lowlevelil.LowLevelILCmpSlt") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpUge`](#binaryninja.lowlevelil.LowLevelILCmpUge "binaryninja.lowlevelil.LowLevelILCmpUge") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpUgt`](#binaryninja.lowlevelil.LowLevelILCmpUgt "binaryninja.lowlevelil.LowLevelILCmpUgt") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpUle`](#binaryninja.lowlevelil.LowLevelILCmpUle "binaryninja.lowlevelil.LowLevelILCmpUle") |  |
| [`binaryninja.lowlevelil.LowLevelILCmpUlt`](#binaryninja.lowlevelil.LowLevelILCmpUlt "binaryninja.lowlevelil.LowLevelILCmpUlt") |  |
| [`binaryninja.lowlevelil.LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase "binaryninja.lowlevelil.LowLevelILComparisonBase") |  |
| [`binaryninja.lowlevelil.LowLevelILConst`](#binaryninja.lowlevelil.LowLevelILConst "binaryninja.lowlevelil.LowLevelILConst") |  |
| [`binaryninja.lowlevelil.LowLevelILConstPtr`](#binaryninja.lowlevelil.LowLevelILConstPtr "binaryninja.lowlevelil.LowLevelILConstPtr") |  |
| [`binaryninja.lowlevelil.LowLevelILConstantBase`](#binaryninja.lowlevelil.LowLevelILConstantBase "binaryninja.lowlevelil.LowLevelILConstantBase") |  |
| [`binaryninja.lowlevelil.LowLevelILDivs`](#binaryninja.lowlevelil.LowLevelILDivs "binaryninja.lowlevelil.LowLevelILDivs") |  |
| [`binaryninja.lowlevelil.LowLevelILDivsDp`](#binaryninja.lowlevelil.LowLevelILDivsDp "binaryninja.lowlevelil.LowLevelILDivsDp") |  |
| [`binaryninja.lowlevelil.LowLevelILDivu`](#binaryninja.lowlevelil.LowLevelILDivu "binaryninja.lowlevelil.LowLevelILDivu") |  |
| [`binaryninja.lowlevelil.LowLevelILDivuDp`](#binaryninja.lowlevelil.LowLevelILDivuDp "binaryninja.lowlevelil.LowLevelILDivuDp") |  |
| [`binaryninja.lowlevelil.LowLevelILExpr`](#binaryninja.lowlevelil.LowLevelILExpr "binaryninja.lowlevelil.LowLevelILExpr") | `class LowLevelILExpr` hold the index of IL Expressions. |
| [`binaryninja.lowlevelil.LowLevelILExternPtr`](#binaryninja.lowlevelil.LowLevelILExternPtr "binaryninja.lowlevelil.LowLevelILExternPtr") |  |
| [`binaryninja.lowlevelil.LowLevelILFabs`](#binaryninja.lowlevelil.LowLevelILFabs "binaryninja.lowlevelil.LowLevelILFabs") |  |
| [`binaryninja.lowlevelil.LowLevelILFadd`](#binaryninja.lowlevelil.LowLevelILFadd "binaryninja.lowlevelil.LowLevelILFadd") |  |
| [`binaryninja.lowlevelil.LowLevelILFcmpE`](#binaryninja.lowlevelil.LowLevelILFcmpE "binaryninja.lowlevelil.LowLevelILFcmpE") |  |
| [`binaryninja.lowlevelil.LowLevelILFcmpGe`](#binaryninja.lowlevelil.LowLevelILFcmpGe "binaryninja.lowlevelil.LowLevelILFcmpGe") |  |
| [`binaryninja.lowlevelil.LowLevelILFcmpGt`](#binaryninja.lowlevelil.LowLevelILFcmpGt "binaryninja.lowlevelil.LowLevelILFcmpGt") |  |
| [`binaryninja.lowlevelil.LowLevelILFcmpLe`](#binaryninja.lowlevelil.LowLevelILFcmpLe "binaryninja.lowlevelil.LowLevelILFcmpLe") |  |
| [`binaryninja.lowlevelil.LowLevelILFcmpLt`](#binaryninja.lowlevelil.LowLevelILFcmpLt "binaryninja.lowlevelil.LowLevelILFcmpLt") |  |
| [`binaryninja.lowlevelil.LowLevelILFcmpNe`](#binaryninja.lowlevelil.LowLevelILFcmpNe "binaryninja.lowlevelil.LowLevelILFcmpNe") |  |
| [`binaryninja.lowlevelil.LowLevelILFcmpO`](#binaryninja.lowlevelil.LowLevelILFcmpO "binaryninja.lowlevelil.LowLevelILFcmpO") |  |
| [`binaryninja.lowlevelil.LowLevelILFcmpUo`](#binaryninja.lowlevelil.LowLevelILFcmpUo "binaryninja.lowlevelil.LowLevelILFcmpUo") |  |
| [`binaryninja.lowlevelil.LowLevelILFdiv`](#binaryninja.lowlevelil.LowLevelILFdiv "binaryninja.lowlevelil.LowLevelILFdiv") |  |
| [`binaryninja.lowlevelil.LowLevelILFlag`](#binaryninja.lowlevelil.LowLevelILFlag "binaryninja.lowlevelil.LowLevelILFlag") |  |
| [`binaryninja.lowlevelil.LowLevelILFlagBit`](#binaryninja.lowlevelil.LowLevelILFlagBit "binaryninja.lowlevelil.LowLevelILFlagBit") |  |
| [`binaryninja.lowlevelil.LowLevelILFlagBitSsa`](#binaryninja.lowlevelil.LowLevelILFlagBitSsa "binaryninja.lowlevelil.LowLevelILFlagBitSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILFlagCond`](#binaryninja.lowlevelil.LowLevelILFlagCond "binaryninja.lowlevelil.LowLevelILFlagCond") |  |
| [`binaryninja.lowlevelil.LowLevelILFlagGroup`](#binaryninja.lowlevelil.LowLevelILFlagGroup "binaryninja.lowlevelil.LowLevelILFlagGroup") |  |
| [`binaryninja.lowlevelil.LowLevelILFlagPhi`](#binaryninja.lowlevelil.LowLevelILFlagPhi "binaryninja.lowlevelil.LowLevelILFlagPhi") |  |
| [`binaryninja.lowlevelil.LowLevelILFlagSsa`](#binaryninja.lowlevelil.LowLevelILFlagSsa "binaryninja.lowlevelil.LowLevelILFlagSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILFloatConst`](#binaryninja.lowlevelil.LowLevelILFloatConst "binaryninja.lowlevelil.LowLevelILFloatConst") |  |
| [`binaryninja.lowlevelil.LowLevelILFloatConv`](#binaryninja.lowlevelil.LowLevelILFloatConv "binaryninja.lowlevelil.LowLevelILFloatConv") |  |
| [`binaryninja.lowlevelil.LowLevelILFloatToInt`](#binaryninja.lowlevelil.LowLevelILFloatToInt "binaryninja.lowlevelil.LowLevelILFloatToInt") |  |
| [`binaryninja.lowlevelil.LowLevelILFloor`](#binaryninja.lowlevelil.LowLevelILFloor "binaryninja.lowlevelil.LowLevelILFloor") |  |
| [`binaryninja.lowlevelil.LowLevelILFmul`](#binaryninja.lowlevelil.LowLevelILFmul "binaryninja.lowlevelil.LowLevelILFmul") |  |
| [`binaryninja.lowlevelil.LowLevelILFneg`](#binaryninja.lowlevelil.LowLevelILFneg "binaryninja.lowlevelil.LowLevelILFneg") |  |
| [`binaryninja.lowlevelil.LowLevelILForceVer`](#binaryninja.lowlevelil.LowLevelILForceVer "binaryninja.lowlevelil.LowLevelILForceVer") |  |
| [`binaryninja.lowlevelil.LowLevelILForceVerSsa`](#binaryninja.lowlevelil.LowLevelILForceVerSsa "binaryninja.lowlevelil.LowLevelILForceVerSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILFsqrt`](#binaryninja.lowlevelil.LowLevelILFsqrt "binaryninja.lowlevelil.LowLevelILFsqrt") |  |
| [`binaryninja.lowlevelil.LowLevelILFsub`](#binaryninja.lowlevelil.LowLevelILFsub "binaryninja.lowlevelil.LowLevelILFsub") |  |
| [`binaryninja.lowlevelil.LowLevelILFtrunc`](#binaryninja.lowlevelil.LowLevelILFtrunc "binaryninja.lowlevelil.LowLevelILFtrunc") |  |
| [`binaryninja.lowlevelil.LowLevelILFunction`](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction") | `class LowLevelILFunction` contains the list of ExpressionIndex objects that make up a function. |
| [`binaryninja.lowlevelil.LowLevelILGoto`](#binaryninja.lowlevelil.LowLevelILGoto "binaryninja.lowlevelil.LowLevelILGoto") |  |
| [`binaryninja.lowlevelil.LowLevelILIf`](#binaryninja.lowlevelil.LowLevelILIf "binaryninja.lowlevelil.LowLevelILIf") |  |
| [`binaryninja.lowlevelil.LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | `class LowLevelILInstruction` Low Level Intermediate Language Instructions are infinite length… |
| [`binaryninja.lowlevelil.LowLevelILIntToFloat`](#binaryninja.lowlevelil.LowLevelILIntToFloat "binaryninja.lowlevelil.LowLevelILIntToFloat") |  |
| [`binaryninja.lowlevelil.LowLevelILIntrinsic`](#binaryninja.lowlevelil.LowLevelILIntrinsic "binaryninja.lowlevelil.LowLevelILIntrinsic") |  |
| [`binaryninja.lowlevelil.LowLevelILIntrinsicSsa`](#binaryninja.lowlevelil.LowLevelILIntrinsicSsa "binaryninja.lowlevelil.LowLevelILIntrinsicSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILJump`](#binaryninja.lowlevelil.LowLevelILJump "binaryninja.lowlevelil.LowLevelILJump") |  |
| [`binaryninja.lowlevelil.LowLevelILJumpTo`](#binaryninja.lowlevelil.LowLevelILJumpTo "binaryninja.lowlevelil.LowLevelILJumpTo") |  |
| [`binaryninja.lowlevelil.LowLevelILLabel`](#binaryninja.lowlevelil.LowLevelILLabel "binaryninja.lowlevelil.LowLevelILLabel") |  |
| [`binaryninja.lowlevelil.LowLevelILLoad`](#binaryninja.lowlevelil.LowLevelILLoad "binaryninja.lowlevelil.LowLevelILLoad") |  |
| [`binaryninja.lowlevelil.LowLevelILLoadSsa`](#binaryninja.lowlevelil.LowLevelILLoadSsa "binaryninja.lowlevelil.LowLevelILLoadSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILLowPart`](#binaryninja.lowlevelil.LowLevelILLowPart "binaryninja.lowlevelil.LowLevelILLowPart") |  |
| [`binaryninja.lowlevelil.LowLevelILLsl`](#binaryninja.lowlevelil.LowLevelILLsl "binaryninja.lowlevelil.LowLevelILLsl") |  |
| [`binaryninja.lowlevelil.LowLevelILLsr`](#binaryninja.lowlevelil.LowLevelILLsr "binaryninja.lowlevelil.LowLevelILLsr") |  |
| [`binaryninja.lowlevelil.LowLevelILMemPhi`](#binaryninja.lowlevelil.LowLevelILMemPhi "binaryninja.lowlevelil.LowLevelILMemPhi") |  |
| [`binaryninja.lowlevelil.LowLevelILMemoryIntrinsicOutputSsa`](#binaryninja.lowlevelil.LowLevelILMemoryIntrinsicOutputSsa "binaryninja.lowlevelil.LowLevelILMemoryIntrinsicOutputSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILMemoryIntrinsicSsa`](#binaryninja.lowlevelil.LowLevelILMemoryIntrinsicSsa "binaryninja.lowlevelil.LowLevelILMemoryIntrinsicSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILMods`](#binaryninja.lowlevelil.LowLevelILMods "binaryninja.lowlevelil.LowLevelILMods") |  |
| [`binaryninja.lowlevelil.LowLevelILModsDp`](#binaryninja.lowlevelil.LowLevelILModsDp "binaryninja.lowlevelil.LowLevelILModsDp") |  |
| [`binaryninja.lowlevelil.LowLevelILModu`](#binaryninja.lowlevelil.LowLevelILModu "binaryninja.lowlevelil.LowLevelILModu") |  |
| [`binaryninja.lowlevelil.LowLevelILModuDp`](#binaryninja.lowlevelil.LowLevelILModuDp "binaryninja.lowlevelil.LowLevelILModuDp") |  |
| [`binaryninja.lowlevelil.LowLevelILMul`](#binaryninja.lowlevelil.LowLevelILMul "binaryninja.lowlevelil.LowLevelILMul") |  |
| [`binaryninja.lowlevelil.LowLevelILMulsDp`](#binaryninja.lowlevelil.LowLevelILMulsDp "binaryninja.lowlevelil.LowLevelILMulsDp") |  |
| [`binaryninja.lowlevelil.LowLevelILMuluDp`](#binaryninja.lowlevelil.LowLevelILMuluDp "binaryninja.lowlevelil.LowLevelILMuluDp") |  |
| [`binaryninja.lowlevelil.LowLevelILNeg`](#binaryninja.lowlevelil.LowLevelILNeg "binaryninja.lowlevelil.LowLevelILNeg") |  |
| [`binaryninja.lowlevelil.LowLevelILNop`](#binaryninja.lowlevelil.LowLevelILNop "binaryninja.lowlevelil.LowLevelILNop") |  |
| [`binaryninja.lowlevelil.LowLevelILNoret`](#binaryninja.lowlevelil.LowLevelILNoret "binaryninja.lowlevelil.LowLevelILNoret") |  |
| [`binaryninja.lowlevelil.LowLevelILNot`](#binaryninja.lowlevelil.LowLevelILNot "binaryninja.lowlevelil.LowLevelILNot") |  |
| [`binaryninja.lowlevelil.LowLevelILOperationAndSize`](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") |  |
| [`binaryninja.lowlevelil.LowLevelILOr`](#binaryninja.lowlevelil.LowLevelILOr "binaryninja.lowlevelil.LowLevelILOr") |  |
| [`binaryninja.lowlevelil.LowLevelILPop`](#binaryninja.lowlevelil.LowLevelILPop "binaryninja.lowlevelil.LowLevelILPop") |  |
| [`binaryninja.lowlevelil.LowLevelILPush`](#binaryninja.lowlevelil.LowLevelILPush "binaryninja.lowlevelil.LowLevelILPush") |  |
| [`binaryninja.lowlevelil.LowLevelILReg`](#binaryninja.lowlevelil.LowLevelILReg "binaryninja.lowlevelil.LowLevelILReg") |  |
| [`binaryninja.lowlevelil.LowLevelILRegPhi`](#binaryninja.lowlevelil.LowLevelILRegPhi "binaryninja.lowlevelil.LowLevelILRegPhi") |  |
| [`binaryninja.lowlevelil.LowLevelILRegSplit`](#binaryninja.lowlevelil.LowLevelILRegSplit "binaryninja.lowlevelil.LowLevelILRegSplit") |  |
| [`binaryninja.lowlevelil.LowLevelILRegSplitDestSsa`](#binaryninja.lowlevelil.LowLevelILRegSplitDestSsa "binaryninja.lowlevelil.LowLevelILRegSplitDestSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILRegSplitSsa`](#binaryninja.lowlevelil.LowLevelILRegSplitSsa "binaryninja.lowlevelil.LowLevelILRegSplitSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILRegSsa`](#binaryninja.lowlevelil.LowLevelILRegSsa "binaryninja.lowlevelil.LowLevelILRegSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILRegSsaPartial`](#binaryninja.lowlevelil.LowLevelILRegSsaPartial "binaryninja.lowlevelil.LowLevelILRegSsaPartial") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackAbsSsa`](#binaryninja.lowlevelil.LowLevelILRegStackAbsSsa "binaryninja.lowlevelil.LowLevelILRegStackAbsSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackDestSsa`](#binaryninja.lowlevelil.LowLevelILRegStackDestSsa "binaryninja.lowlevelil.LowLevelILRegStackDestSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackFreeAbsSsa`](#binaryninja.lowlevelil.LowLevelILRegStackFreeAbsSsa "binaryninja.lowlevelil.LowLevelILRegStackFreeAbsSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackFreeReg`](#binaryninja.lowlevelil.LowLevelILRegStackFreeReg "binaryninja.lowlevelil.LowLevelILRegStackFreeReg") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackFreeRel`](#binaryninja.lowlevelil.LowLevelILRegStackFreeRel "binaryninja.lowlevelil.LowLevelILRegStackFreeRel") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackFreeRelSsa`](#binaryninja.lowlevelil.LowLevelILRegStackFreeRelSsa "binaryninja.lowlevelil.LowLevelILRegStackFreeRelSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackPhi`](#binaryninja.lowlevelil.LowLevelILRegStackPhi "binaryninja.lowlevelil.LowLevelILRegStackPhi") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackPop`](#binaryninja.lowlevelil.LowLevelILRegStackPop "binaryninja.lowlevelil.LowLevelILRegStackPop") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackPush`](#binaryninja.lowlevelil.LowLevelILRegStackPush "binaryninja.lowlevelil.LowLevelILRegStackPush") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackRel`](#binaryninja.lowlevelil.LowLevelILRegStackRel "binaryninja.lowlevelil.LowLevelILRegStackRel") |  |
| [`binaryninja.lowlevelil.LowLevelILRegStackRelSsa`](#binaryninja.lowlevelil.LowLevelILRegStackRelSsa "binaryninja.lowlevelil.LowLevelILRegStackRelSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILRet`](#binaryninja.lowlevelil.LowLevelILRet "binaryninja.lowlevelil.LowLevelILRet") |  |
| [`binaryninja.lowlevelil.LowLevelILRlc`](#binaryninja.lowlevelil.LowLevelILRlc "binaryninja.lowlevelil.LowLevelILRlc") |  |
| [`binaryninja.lowlevelil.LowLevelILRol`](#binaryninja.lowlevelil.LowLevelILRol "binaryninja.lowlevelil.LowLevelILRol") |  |
| [`binaryninja.lowlevelil.LowLevelILRor`](#binaryninja.lowlevelil.LowLevelILRor "binaryninja.lowlevelil.LowLevelILRor") |  |
| [`binaryninja.lowlevelil.LowLevelILRoundToInt`](#binaryninja.lowlevelil.LowLevelILRoundToInt "binaryninja.lowlevelil.LowLevelILRoundToInt") |  |
| [`binaryninja.lowlevelil.LowLevelILRrc`](#binaryninja.lowlevelil.LowLevelILRrc "binaryninja.lowlevelil.LowLevelILRrc") |  |
| [`binaryninja.lowlevelil.LowLevelILSbb`](#binaryninja.lowlevelil.LowLevelILSbb "binaryninja.lowlevelil.LowLevelILSbb") |  |
| [`binaryninja.lowlevelil.LowLevelILSeparateParamListSsa`](#binaryninja.lowlevelil.LowLevelILSeparateParamListSsa "binaryninja.lowlevelil.LowLevelILSeparateParamListSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILSetFlag`](#binaryninja.lowlevelil.LowLevelILSetFlag "binaryninja.lowlevelil.LowLevelILSetFlag") |  |
| [`binaryninja.lowlevelil.LowLevelILSetFlagSsa`](#binaryninja.lowlevelil.LowLevelILSetFlagSsa "binaryninja.lowlevelil.LowLevelILSetFlagSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILSetReg`](#binaryninja.lowlevelil.LowLevelILSetReg "binaryninja.lowlevelil.LowLevelILSetReg") |  |
| [`binaryninja.lowlevelil.LowLevelILSetRegSplit`](#binaryninja.lowlevelil.LowLevelILSetRegSplit "binaryninja.lowlevelil.LowLevelILSetRegSplit") |  |
| [`binaryninja.lowlevelil.LowLevelILSetRegSplitSsa`](#binaryninja.lowlevelil.LowLevelILSetRegSplitSsa "binaryninja.lowlevelil.LowLevelILSetRegSplitSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILSetRegSsa`](#binaryninja.lowlevelil.LowLevelILSetRegSsa "binaryninja.lowlevelil.LowLevelILSetRegSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILSetRegSsaPartial`](#binaryninja.lowlevelil.LowLevelILSetRegSsaPartial "binaryninja.lowlevelil.LowLevelILSetRegSsaPartial") |  |
| [`binaryninja.lowlevelil.LowLevelILSetRegStackAbsSsa`](#binaryninja.lowlevelil.LowLevelILSetRegStackAbsSsa "binaryninja.lowlevelil.LowLevelILSetRegStackAbsSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILSetRegStackRel`](#binaryninja.lowlevelil.LowLevelILSetRegStackRel "binaryninja.lowlevelil.LowLevelILSetRegStackRel") |  |
| [`binaryninja.lowlevelil.LowLevelILSetRegStackRelSsa`](#binaryninja.lowlevelil.LowLevelILSetRegStackRelSsa "binaryninja.lowlevelil.LowLevelILSetRegStackRelSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILSharedParamSlotSsa`](#binaryninja.lowlevelil.LowLevelILSharedParamSlotSsa "binaryninja.lowlevelil.LowLevelILSharedParamSlotSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILStore`](#binaryninja.lowlevelil.LowLevelILStore "binaryninja.lowlevelil.LowLevelILStore") |  |
| [`binaryninja.lowlevelil.LowLevelILStoreSsa`](#binaryninja.lowlevelil.LowLevelILStoreSsa "binaryninja.lowlevelil.LowLevelILStoreSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILSub`](#binaryninja.lowlevelil.LowLevelILSub "binaryninja.lowlevelil.LowLevelILSub") |  |
| [`binaryninja.lowlevelil.LowLevelILSx`](#binaryninja.lowlevelil.LowLevelILSx "binaryninja.lowlevelil.LowLevelILSx") |  |
| [`binaryninja.lowlevelil.LowLevelILSyscall`](#binaryninja.lowlevelil.LowLevelILSyscall "binaryninja.lowlevelil.LowLevelILSyscall") |  |
| [`binaryninja.lowlevelil.LowLevelILSyscallSsa`](#binaryninja.lowlevelil.LowLevelILSyscallSsa "binaryninja.lowlevelil.LowLevelILSyscallSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILTailcall`](#binaryninja.lowlevelil.LowLevelILTailcall "binaryninja.lowlevelil.LowLevelILTailcall") |  |
| [`binaryninja.lowlevelil.LowLevelILTailcallSsa`](#binaryninja.lowlevelil.LowLevelILTailcallSsa "binaryninja.lowlevelil.LowLevelILTailcallSsa") |  |
| [`binaryninja.lowlevelil.LowLevelILTestBit`](#binaryninja.lowlevelil.LowLevelILTestBit "binaryninja.lowlevelil.LowLevelILTestBit") |  |
| [`binaryninja.lowlevelil.LowLevelILTrap`](#binaryninja.lowlevelil.LowLevelILTrap "binaryninja.lowlevelil.LowLevelILTrap") |  |
| [`binaryninja.lowlevelil.LowLevelILUnaryBase`](#binaryninja.lowlevelil.LowLevelILUnaryBase "binaryninja.lowlevelil.LowLevelILUnaryBase") |  |
| [`binaryninja.lowlevelil.LowLevelILUndef`](#binaryninja.lowlevelil.LowLevelILUndef "binaryninja.lowlevelil.LowLevelILUndef") |  |
| [`binaryninja.lowlevelil.LowLevelILUnimpl`](#binaryninja.lowlevelil.LowLevelILUnimpl "binaryninja.lowlevelil.LowLevelILUnimpl") |  |
| [`binaryninja.lowlevelil.LowLevelILUnimplMem`](#binaryninja.lowlevelil.LowLevelILUnimplMem "binaryninja.lowlevelil.LowLevelILUnimplMem") |  |
| [`binaryninja.lowlevelil.LowLevelILXor`](#binaryninja.lowlevelil.LowLevelILXor "binaryninja.lowlevelil.LowLevelILXor") |  |
| [`binaryninja.lowlevelil.LowLevelILZx`](#binaryninja.lowlevelil.LowLevelILZx "binaryninja.lowlevelil.LowLevelILZx") |  |
| [`binaryninja.lowlevelil.SSAFlag`](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") |  |
| [`binaryninja.lowlevelil.SSARegister`](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") |  |
| [`binaryninja.lowlevelil.SSARegisterOrFlag`](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag") |  |
| [`binaryninja.lowlevelil.SSARegisterStack`](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") |  |

| Function | Description |
| --- | --- |
| [`binaryninja.lowlevelil.LLIL_GET_TEMP_REG_INDEX`](#binaryninja.lowlevelil.LLIL_GET_TEMP_REG_INDEX "binaryninja.lowlevelil.LLIL_GET_TEMP_REG_INDEX") |  |
| [`binaryninja.lowlevelil.LLIL_REG_IS_TEMP`](#binaryninja.lowlevelil.LLIL_REG_IS_TEMP "binaryninja.lowlevelil.LLIL_REG_IS_TEMP") |  |
| [`binaryninja.lowlevelil.LLIL_TEMP`](#binaryninja.lowlevelil.LLIL_TEMP "binaryninja.lowlevelil.LLIL_TEMP") |  |

## CoreLowLevelILInstruction

*class* CoreLowLevelILInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#CoreLowLevelILInstruction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    CoreLowLevelILInstruction(operation: binaryninja.enums.LowLevelILOperation, attributes:
    int, size: int, flags: int, source_operand: <function NewType.<locals>.new_type at
    0x10a719790>, operands: Tuple[ExpressionIndex, ExpressionIndex, ExpressionIndex,
    ExpressionIndex], address: int)

    __init__(*operation: [LowLevelILOperation](enums.md#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation")*, *attributes: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flags: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *source_operand: ExpressionIndex*, *operands: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **operation** ([*LowLevelILOperation*](enums.md#binaryninja.enums.LowLevelILOperation
              "binaryninja.enums.LowLevelILOperation")) –
            - **attributes** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **flags** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **source_operand** (*ExpressionIndex*) –
            - **operands** ([*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple "(in
              Python v3.14)")*[**ExpressionIndex**,* *ExpressionIndex**,* *ExpressionIndex**,*
              *ExpressionIndex**]*) –
            - **address** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    *classmethod* from_BNLowLevelILInstruction(*instr: BNLowLevelILInstruction*) → [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#CoreLowLevelILInstruction.from_BNLowLevelILInstruction)
    :   Parameters:
        :   **instr** (*BNLowLevelILInstruction*) –

        Return type:
        :   [*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
            "binaryninja.lowlevelil.CoreLowLevelILInstruction")

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    attributes*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    flags*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    operands*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*

    operation*: [LowLevelILOperation](enums.md#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    source_operand*: ExpressionIndex*

## ILFlag

*class* ILFlag[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#ILFlag)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ILFlag(arch: ‘architecture.Architecture’, index: ‘architecture.FlagIndex’)

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *index: FlagIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **index** (*FlagIndex*) –

        Return type:
        :   *None*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    index*: FlagIndex*

    *property* name*: FlagName*

    *property* temp*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

## ILIntrinsic

*class* ILIntrinsic[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#ILIntrinsic)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ILIntrinsic(arch: ‘architecture.Architecture’, index: ‘architecture.IntrinsicIndex’)

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *index: IntrinsicIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **index** (*IntrinsicIndex*) –

        Return type:
        :   *None*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    index*: IntrinsicIndex*

    *property* inputs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[IntrinsicInput](architecture.md#binaryninja.architecture.IntrinsicInput "binaryninja.architecture.IntrinsicInput")]*
    :   `inputs` is only available if the IL intrinsic is an Architecture intrinsic

    *property* name*: IntrinsicName*

    *property* outputs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Type](types.md#binaryninja.types.Type "binaryninja.types.Type")]*
    :   `outputs` is only available if the IL intrinsic is an Architecture intrinsic

## ILRegister

*class* ILRegister[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#ILRegister)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ILRegister(arch: ‘architecture.Architecture’, index: ‘architecture.RegisterIndex’)

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *index: RegisterIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **index** (*RegisterIndex*) –

        Return type:
        :   *None*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    index*: RegisterIndex*

    *property* info*: [RegisterInfo](architecture.md#binaryninja.architecture.RegisterInfo "binaryninja.architecture.RegisterInfo")*

    *property* name*: RegisterName*

    *property* temp*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

## ILRegisterStack

*class* ILRegisterStack[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#ILRegisterStack)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ILRegisterStack(arch: ‘architecture.Architecture’, index:
    ‘architecture.RegisterStackIndex’)

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *index: RegisterStackIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **index** (*RegisterStackIndex*) –

        Return type:
        :   *None*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    index*: RegisterStackIndex*

    *property* info*: [RegisterStackInfo](architecture.md#binaryninja.architecture.RegisterStackInfo "binaryninja.architecture.RegisterStackInfo")*

    *property* name*: RegisterStackName*

## ILSemanticFlagClass

*class* ILSemanticFlagClass[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#ILSemanticFlagClass)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ILSemanticFlagClass(arch: ‘architecture.Architecture’, index:
    ‘architecture.SemanticClassIndex’)

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *index: SemanticClassIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **index** (*SemanticClassIndex*) –

        Return type:
        :   *None*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    index*: SemanticClassIndex*

    *property* name*: SemanticClassName*

## ILSemanticFlagGroup

*class* ILSemanticFlagGroup[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#ILSemanticFlagGroup)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    ILSemanticFlagGroup(arch: ‘architecture.Architecture’, index:
    ‘architecture.SemanticGroupIndex’)

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *index: SemanticGroupIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **index** (*SemanticGroupIndex*) –

        Return type:
        :   *None*

    arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    index*: SemanticGroupIndex*

    *property* name*: SemanticGroupName*

## LowLevelILAdc

*class* LowLevelILAdc[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILAdc)
:   Bases: [`LowLevelILCarryBase`](#binaryninja.lowlevelil.LowLevelILCarryBase
    "binaryninja.lowlevelil.LowLevelILCarryBase")

    LowLevelILAdc(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILAdd

*class* LowLevelILAdd[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILAdd)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILAdd(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILAddOverflow

*class* LowLevelILAddOverflow[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILAddOverflow)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILAddOverflow(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILAnd

*class* LowLevelILAnd[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILAnd)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILAnd(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILAsr

*class* LowLevelILAsr[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILAsr)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILAsr(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILAssert

*class* LowLevelILAssert[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILAssert)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILAssert(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* constraint*: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

## LowLevelILAssertSsa

*class* LowLevelILAssertSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILAssertSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILAssertSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* constraint*: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

## LowLevelILBasicBlock

*class* LowLevelILBasicBlock[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILBasicBlock)
:   Bases: [`BasicBlock`](basicblock.md#binaryninja.basicblock.BasicBlock
    "binaryninja.basicblock.BasicBlock")

    The `LogLevelILBasicBlock` object is returned during analysis and should not be directly
    instantiated.

    __init__(*handle: LP_BNBasicBlock*, *owner: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILBasicBlock.__init__)
    :   Parameters:
        :   - **handle** (*LP_BNBasicBlock*) –
            - **owner** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*) –

    *property* il_function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*
    :   IL Function of which this block is a part, if the block is part of an IL Function.

    *property* instruction_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LowLevelILBinaryBase

*class* LowLevelILBinaryBase[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILBinaryBase)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`BinaryOperation`](commonil.md#binaryninja.commonil.BinaryOperation
    "binaryninja.commonil.BinaryOperation")

    LowLevelILBinaryBase(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* left*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* right*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILBoolToInt

*class* LowLevelILBoolToInt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILBoolToInt)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILBoolToInt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILBp

*class* LowLevelILBp[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILBp)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    LowLevelILBp(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCall

*class* LowLevelILCall[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCall)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Localcall`](commonil.md#binaryninja.commonil.Localcall
    "binaryninja.commonil.Localcall")

    LowLevelILCall(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCallOutputSsa

*class* LowLevelILCallOutputSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCallOutputSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILCallOutputSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCallParam

*class* LowLevelILCallParam[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCallParam)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILCallParam(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

## LowLevelILCallSsa

*class* LowLevelILCallSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCallSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Localcall`](commonil.md#binaryninja.commonil.Localcall
    "binaryninja.commonil.Localcall"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    LowLevelILCallSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*

    *property* param*: [LowLevelILCallParam](#binaryninja.lowlevelil.LowLevelILCallParam "binaryninja.lowlevelil.LowLevelILCallParam")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

    *property* stack*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILCallStackAdjust

*class* LowLevelILCallStackAdjust[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCallStackAdjust)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Localcall`](commonil.md#binaryninja.commonil.Localcall
    "binaryninja.commonil.Localcall")

    LowLevelILCallStackAdjust(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* reg_stack_adjustments*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

    *property* stack_adjustment*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LowLevelILCallStackSsa

*class* LowLevelILCallStackSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCallStackSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILCallStackSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LowLevelILCarryBase

*class* LowLevelILCarryBase[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCarryBase)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Carry`](commonil.md#binaryninja.commonil.Carry "binaryninja.commonil.Carry")

    LowLevelILCarryBase(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* carry*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* left*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* right*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILCeil

*class* LowLevelILCeil[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCeil)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILCeil(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILCmpE

*class* LowLevelILCmpE[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpE)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase")

    LowLevelILCmpE(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCmpNe

*class* LowLevelILCmpNe[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpNe)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase")

    LowLevelILCmpNe(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCmpSge

*class* LowLevelILCmpSge[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpSge)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    LowLevelILCmpSge(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCmpSgt

*class* LowLevelILCmpSgt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpSgt)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    LowLevelILCmpSgt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCmpSle

*class* LowLevelILCmpSle[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpSle)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    LowLevelILCmpSle(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCmpSlt

*class* LowLevelILCmpSlt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpSlt)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    LowLevelILCmpSlt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCmpUge

*class* LowLevelILCmpUge[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpUge)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase")

    LowLevelILCmpUge(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCmpUgt

*class* LowLevelILCmpUgt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpUgt)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase")

    LowLevelILCmpUgt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCmpUle

*class* LowLevelILCmpUle[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpUle)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase")

    LowLevelILCmpUle(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILCmpUlt

*class* LowLevelILCmpUlt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILCmpUlt)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase")

    LowLevelILCmpUlt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILComparisonBase

*class* LowLevelILComparisonBase[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILComparisonBase)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Comparison`](commonil.md#binaryninja.commonil.Comparison
    "binaryninja.commonil.Comparison")

    LowLevelILComparisonBase(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILConst

*class* LowLevelILConst[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILConst)
:   Bases: [`LowLevelILConstantBase`](#binaryninja.lowlevelil.LowLevelILConstantBase
    "binaryninja.lowlevelil.LowLevelILConstantBase")

    LowLevelILConst(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILConstPtr

*class* LowLevelILConstPtr[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILConstPtr)
:   Bases: [`LowLevelILConstantBase`](#binaryninja.lowlevelil.LowLevelILConstantBase
    "binaryninja.lowlevelil.LowLevelILConstantBase")

    LowLevelILConstPtr(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILConstantBase

*class* LowLevelILConstantBase[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILConstantBase)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Constant`](commonil.md#binaryninja.commonil.Constant "binaryninja.commonil.Constant")

    LowLevelILConstantBase(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILDivs

*class* LowLevelILDivs[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILDivs)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"), [`Signed`](commonil.md#binaryninja.commonil.Signed
    "binaryninja.commonil.Signed")

    LowLevelILDivs(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILDivsDp

*class* LowLevelILDivsDp[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILDivsDp)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    LowLevelILDivsDp(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILDivu

*class* LowLevelILDivu[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILDivu)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILDivu(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILDivuDp

*class* LowLevelILDivuDp[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILDivuDp)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    LowLevelILDivuDp(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILExpr

*class* LowLevelILExpr[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILExpr)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class LowLevelILExpr` hold the index of IL Expressions.

    Note

    Deprecated. Use ExpressionIndex instead

    __init__(*index: ExpressionIndex*)[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILExpr.__init__)
    :   Parameters:
        :   **index** (*ExpressionIndex*) –

    *property* index*: ExpressionIndex*

## LowLevelILExternPtr

*class* LowLevelILExternPtr[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILExternPtr)
:   Bases: [`LowLevelILConstantBase`](#binaryninja.lowlevelil.LowLevelILConstantBase
    "binaryninja.lowlevelil.LowLevelILConstantBase")

    LowLevelILExternPtr(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LowLevelILFabs

*class* LowLevelILFabs[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFabs)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILFabs(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILFadd

*class* LowLevelILFadd[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFadd)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFadd(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFcmpE

*class* LowLevelILFcmpE[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFcmpE)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFcmpE(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFcmpGe

*class* LowLevelILFcmpGe[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFcmpGe)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFcmpGe(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFcmpGt

*class* LowLevelILFcmpGt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFcmpGt)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFcmpGt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFcmpLe

*class* LowLevelILFcmpLe[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFcmpLe)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFcmpLe(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFcmpLt

*class* LowLevelILFcmpLt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFcmpLt)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFcmpLt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFcmpNe

*class* LowLevelILFcmpNe[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFcmpNe)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFcmpNe(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFcmpO

*class* LowLevelILFcmpO[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFcmpO)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFcmpO(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFcmpUo

*class* LowLevelILFcmpUo[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFcmpUo)
:   Bases: [`LowLevelILComparisonBase`](#binaryninja.lowlevelil.LowLevelILComparisonBase
    "binaryninja.lowlevelil.LowLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFcmpUo(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFdiv

*class* LowLevelILFdiv[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFdiv)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFdiv(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFlag

*class* LowLevelILFlag[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFlag)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILFlag(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag")*

## LowLevelILFlagBit

*class* LowLevelILFlagBit[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFlagBit)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILFlagBit(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* bit*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag")*

## LowLevelILFlagBitSsa

*class* LowLevelILFlagBitSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFlagBitSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILFlagBitSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* bit*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")*

## LowLevelILFlagCond

*class* LowLevelILFlagCond[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFlagCond)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILFlagCond(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* condition*: [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* semantic_class*: [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFlagGroup

*class* LowLevelILFlagGroup[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFlagGroup)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILFlagGroup(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* semantic_group*: [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup")*

## LowLevelILFlagPhi

*class* LowLevelILFlagPhi[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFlagPhi)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Phi`](commonil.md#binaryninja.commonil.Phi "binaryninja.commonil.Phi")

    LowLevelILFlagPhi(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")]*

## LowLevelILFlagSsa

*class* LowLevelILFlagSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFlagSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILFlagSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")*

## LowLevelILFloatConst

*class* LowLevelILFloatConst[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFloatConst)
:   Bases: [`LowLevelILConstantBase`](#binaryninja.lowlevelil.LowLevelILConstantBase
    "binaryninja.lowlevelil.LowLevelILConstantBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFloatConst(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFloatConv

*class* LowLevelILFloatConv[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFloatConv)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILFloatConv(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILFloatToInt

*class* LowLevelILFloatToInt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFloatToInt)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILFloatToInt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILFloor

*class* LowLevelILFloor[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFloor)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILFloor(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILFmul

*class* LowLevelILFmul[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFmul)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFmul(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFneg

*class* LowLevelILFneg[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFneg)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILFneg(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILForceVer

*class* LowLevelILForceVer[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILForceVer)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILForceVer(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILForceVerSsa

*class* LowLevelILForceVerSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILForceVerSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILForceVerSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

## LowLevelILFsqrt

*class* LowLevelILFsqrt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFsqrt)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILFsqrt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILFsub

*class* LowLevelILFsub[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFsub)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILFsub(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILFtrunc

*class* LowLevelILFtrunc[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFtrunc)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILFtrunc(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILFunction

*class* LowLevelILFunction[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class LowLevelILFunction` contains the list of ExpressionIndex objects that make up a
    function. ExpressionIndex objects can be added to the LowLevelILFunction by calling
    [`append`](#binaryninja.lowlevelil.LowLevelILFunction.append
    "binaryninja.lowlevelil.LowLevelILFunction.append") and passing the result of the
    various class methods which return ExpressionIndex objects.

    LowLevelILFlagCondition values used as parameters in the
    [`flag_condition`](#binaryninja.lowlevelil.LowLevelILFunction.flag_condition
    "binaryninja.lowlevelil.LowLevelILFunction.flag_condition") method.

    > | LowLevelILFlagCondition | Operator | Description |
    > | --- | --- | --- |
    > | LLFC_E | == | Equal |
    > | LLFC_NE | != | Not equal |
    > | LLFC_SLT | s< | Signed less than |
    > | LLFC_ULT | u< | Unsigned less than |
    > | LLFC_SLE | s<= | Signed less than or equal |
    > | LLFC_ULE | u<= | Unsigned less than or equal |
    > | LLFC_SGE | s>= | Signed greater than or equal |
    > | LLFC_UGE | u>= | Unsigned greater than or equal |
    > | LLFC_SGT | s> | Signed greater than |
    > | LLFC_UGT | u> | Unsigned greater than |
    > | LLFC_NEG |  | Negative |
    > | LLFC_POS |  | Positive |
    > | LLFC_O | overflow | Overflow |
    > | LLFC_NO | !overflow | No overflow |

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: BNLowLevelILFunction | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *source_func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.__init__)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **handle** (*BNLowLevelILFunction* *|* *None*) –
            - **source_func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –

    add(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.add)
    :   `add` adds expression `a` to expression `b` potentially setting flags `flags` and
        returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `add.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    add_carry(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.add_carry)
    :   `add_carry` adds with carry expression `a` to expression `b` potentially setting flags
        `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **carry** (*ExpressionIndex*) – Carry flag expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `adc.<size>{<flags>}(a, b, carry)`

        Return type:
        :   ExpressionIndex

    add_index_list(*indices: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.add_index_list)
    :   `add_index_list` returns an index list expression for the given list of integers.

        Parameters:
        :   **indices** (*List**(*[*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")*)*) – list of numbers

        Returns:
        :   an operand list expression

        Return type:
        :   ExpressionIndex

    add_label_for_address(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.add_label_for_address)
    :   `add_label_for_address` adds a low-level IL label for the given architecture `arch` at
        the given virtual address `addr`. This is generally called automatically by the core
        when Lifted IL is being generated, and will be automatically called with the start
        address of every basic block found during disassembly.

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – Architecture to add labels for
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the IL address to add a label at

        Return type:
        :   *None*

    add_label_map(*labels: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [LowLevelILLabel](#binaryninja.lowlevelil.LowLevelILLabel "binaryninja.lowlevelil.LowLevelILLabel")]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.add_label_map)
    :   `add_label_map` returns a label list expression for the given list of LowLevelILLabel
        objects.

        Parameters:
        :   - **labels** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python
              v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")*,* [*LowLevelILLabel*](#binaryninja.lowlevelil.LowLevelILLabel
              "binaryninja.lowlevelil.LowLevelILLabel")*)*) – the list of LowLevelILLabel to get a
              label list expression from
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the label list expression

        Return type:
        :   ExpressionIndex

    add_operand_list(*operands: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.add_operand_list)
    :   `add_operand_list` returns an operand list expression for the given list of integer
        operands.

        Parameters:
        :   **operands** (*List**(**Union**[**ExpressionIndex**,* *ExpressionIndex**]**)*) – list of
            operand numbers

        Returns:
        :   an operand list expression

        Return type:
        :   ExpressionIndex

    and_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.and_expr)
    :   `and_expr` bitwise and’s expression `a` and expression `b` potentially setting flags
        `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `and.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    append(*expr: ExpressionIndex*) → InstructionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.append)
    :   `append` adds the ExpressionIndex `expr` to the current LowLevelILFunction.

        Parameters:
        :   **expr** (*ExpressionIndex*) – the ExpressionIndex to add to the current
            LowLevelILFunction

        Returns:
        :   Index of added instruction in the current function

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    arith_shift_right(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.arith_shift_right)
    :   `arith_shift_right` shifts arithmetic right expression `a` by expression `b` potentially
        setting flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `asr.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    assert_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: architecture.RegisterType*, *constraint: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.assert_expr)
    :   `assert_expr` assert `constraint` is the value of the given register `src`. Used when
        setting user variable values.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of value in the constraint
            - **src** (*RegisterType*) – register to constrain
            - **constraint** ([*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
              "binaryninja.variable.PossibleValueSet")) – asserted value of register
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `ASSERT(reg, constraint)`

        Return type:
        :   ExpressionIndex

    bool_to_int(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.bool_to_int)
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

    breakpoint(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.breakpoint)
    :   `breakpoint` returns a processor breakpoint expression.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a breakpoint expression.

        Return type:
        :   ExpressionIndex

    cache_possible_value_set(*pvs: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.cache_possible_value_set)
    :   Cache a PossibleValueSet in the IL function, returning its index for use in an
        expression operand :param pvs: PossibleValueSet to cache :return: Index of the
        PossibleValueSet in the cache

        Parameters:
        :   **pvs** ([*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    call(*dest: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.call)
    :   `call` returns an expression which (on architectures without a link register) first
        pushes the address of the next instruction onto the stack then jumps (branches) to the
        expression `dest`

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression to call
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `call(dest)`

        Return type:
        :   ExpressionIndex

    call_stack_adjust(*dest: ExpressionIndex*, *stack_adjust: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg_stack_adjustments: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[architecture.RegisterStackType, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.call_stack_adjust)
    :   `call_stack_adjust` returns an expression which (on architectures without a link
        register) first pushes the address of the next instruction onto the stack then jumps
        (branches) to the expression `dest`. After the function exits, `stack_adjust` is added
        to the stack pointer register.

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression to call
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression
            - **stack_adjust** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) –
            - **reg_stack_adjustments**
              ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python
              v3.14)")*[**architecture.RegisterStackType**,*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]* *|*
              *None*) –

        Returns:
        :   The expression `call(dest), stack += stack_adjust`

        Return type:
        :   ExpressionIndex

    ceil(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.ceil)
    :   `ceil` rounds a floating point value to an integer towards positive infinity

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to round up
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `roundint.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    clear_indirect_branches() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.clear_indirect_branches)
    :   Return type:
        :   *None*

    compare_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_equal)
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

    compare_not_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_not_equal)
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

    compare_signed_greater_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_signed_greater_equal)
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

    compare_signed_greater_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_signed_greater_than)
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

    compare_signed_less_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_signed_less_equal)
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

    compare_signed_less_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_signed_less_than)
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

    compare_unsigned_greater_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_unsigned_greater_equal)
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

    compare_unsigned_greater_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_unsigned_greater_than)
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

    compare_unsigned_less_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_unsigned_less_equal)
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

    compare_unsigned_less_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.compare_unsigned_less_than)
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

    const(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.const)
    :   `const` returns an expression for the constant integer `value` with size `size`

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

    const_pointer(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.const_pointer)
    :   `const_pointer` returns an expression for the constant pointer `value` with size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the pointer in bytes
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address referenced by pointer
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    copy_expr(*original: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.copy_expr)
    :   `copy_expr` adds an expression to the function which is equivalent to the given
        expression

        Warning

        This function should ONLY be called as a part of a lifter or workflow. It will otherwise
        not do anything useful as analysis will not be running.

        Parameters:
        :   **original** ([*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")) – the original IL Instruction you want
            to copy

        Returns:
        :   The index of the newly copied expression

        Return type:
        :   ExpressionIndex

    copy_expr_to(*expr: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*, *dest: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *sub_expr_handler: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")], ExpressionIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.copy_expr_to)
    :   `copy_expr_to` deep copies an expression from this function into a target function If
        provided, the function `sub_expr_handler` will be called on every copied sub-expression

        Warning

        This function should ONLY be called as a part of a lifter or workflow. It will otherwise
        not do anything useful as analysis will not be running.

        Parameters:
        :   - **expr** ([*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction")) – Expression in this function to copy
            - **dest** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) – Function to copy the expression to
            - **sub_expr_handler**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction")*]**,* *ExpressionIndex**]* *|* *None*) –
              Optional function to call on every copied sub-expression

        Returns:
        :   Index of the copied expression in the target function

        Return type:
        :   ExpressionIndex

    create_graph(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreFlowGraph](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.create_graph)
    :   Parameters:
        :   **settings**
            ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*CoreFlowGraph*](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph
            "binaryninja.flowgraph.CoreFlowGraph")

    create_graph_immediate(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreFlowGraph](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.create_graph_immediate)
    :   Parameters:
        :   **settings**
            ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*CoreFlowGraph*](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph
            "binaryninja.flowgraph.CoreFlowGraph")

    div_double_prec_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.div_double_prec_signed)
    :   `div_double_prec_signed` signed double precision divide using expression `a` as a single
        double precision register by expression `b` potentially setting flags `flags` and
        returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `divs.dp.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    div_double_prec_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.div_double_prec_unsigned)
    :   `div_double_prec_unsigned` unsigned double precision divide using expression `a` as a
        single double precision register by expression `b` potentially setting flags `flags` and
        returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `divu.dp.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    div_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.div_signed)
    :   `div_signed` signed divide expression `a` by expression `b` potentially setting flags
        `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `divs.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    div_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.div_unsigned)
    :   `div_unsigned` unsigned divide expression `a` by expression `b` potentially setting
        flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `divu.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    expr(*operation*, *a: ExpressionIndex = 0*, *b: ExpressionIndex = 0*, *c: ExpressionIndex = 0*, *d: ExpressionIndex = 0*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *source_location: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.expr)
    :   Parameters:
        :   - **a** (*ExpressionIndex*) –
            - **b** (*ExpressionIndex*) –
            - **c** (*ExpressionIndex*) –
            - **d** (*ExpressionIndex*) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **flags** (*FlagWriteTypeName* *|* *FlagWriteTypeIndex* *|* *None*) –
            - **source_location**
              ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation") *|* *None*) –

        Return type:
        :   ExpressionIndex

    extern_pointer(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.extern_pointer)
    :   `extern_pointer` returns an expression for the constant external pointer `value` with
        size `size` at offset `offset`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the pointer in bytes
            - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – address referenced by pointer
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset into external pointer
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size

        Return type:
        :   ExpressionIndex

    finalize() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.finalize)
    :   `finalize` ends the function and computes the list of basic blocks.

        Return type:
        :   *None*

    flag(*flag: architecture.FlagType*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.flag)
    :   `flag` returns a flag expression for the given flag name.

        Parameters:
        :   - **flag** (*architecture.FlagType*) – flag expression to retrieve
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A flag expression of given flag name

        Return type:
        :   ExpressionIndex

    flag_bit(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flag: architecture.FlagType*, *bit: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.flag_bit)
    :   `flag_bit` sets the flag named `flag` and size `size` to the constant integer value
        `bit`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the flag
            - **flag** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – flag value
            - **bit** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – integer value to set the bit to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A constant expression of given value and size `FLAG.flag = bit`

        Return type:
        :   ExpressionIndex

    flag_condition(*cond: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *sem_class: architecture.SemanticClassType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.flag_condition)
    :   `flag_condition` returns a flag_condition expression for the given
        LowLevelILFlagCondition

        Parameters:
        :   - **cond** ([*LowLevelILFlagCondition*](enums.md#binaryninja.enums.LowLevelILFlagCondition
              "binaryninja.enums.LowLevelILFlagCondition")) – Flag condition expression to retrieve
            - **sem_class** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – Optional semantic flag class
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A flag_condition expression

        Return type:
        :   ExpressionIndex

    flag_group(*sem_group: SemanticGroupName*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.flag_group)
    :   `flag_group` returns a flag_group expression for the given semantic flag group

        Parameters:
        :   - **sem_group** (*SemanticGroupName*) – Semantic flag group to access
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A flag_group expression

        Return type:
        :   ExpressionIndex

    float_abs(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_abs)
    :   `float_abs` returns absolute value of floating point expression `value` of size `size`
        potentially setting flags

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to get the absolute value of
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fabs.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    float_add(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_add)
    :   `float_add` adds floating point expression `a` to expression `b` potentially setting
        flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fadd.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    float_compare_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_compare_equal)
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

    float_compare_greater_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_compare_greater_equal)
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

    float_compare_greater_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_compare_greater_than)
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

    float_compare_less_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_compare_less_equal)
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

    float_compare_less_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_compare_less_than)
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

    float_compare_not_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_compare_not_equal)
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

    float_compare_ordered(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_compare_ordered)
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

    float_compare_unordered(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_compare_unordered)
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

    float_const_double(*value: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_const_double)
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

    float_const_raw(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_const_raw)
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

    float_const_single(*value: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_const_single)
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

    float_convert(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_convert)
    :   `float_convert` converts floating point value of expression `value` to size `size`
        potentially setting flags

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to convert to a float of `size` bytes
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fconvert.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    float_div(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_div)
    :   `float_div` divides floating point expression `a` by expression `b` potentially setting
        flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fdiv.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    float_mult(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_mult)
    :   `float_mult` multiplies floating point expression `a` by expression `b` potentially
        setting flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fmul.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    float_neg(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_neg)
    :   `float_neg` returns sign negation of floating point expression `value` of size `size`
        potentially setting flags

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to negate
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fneg.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    float_sqrt(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_sqrt)
    :   `float_sqrt` returns square root of floating point expression `value` of size `size`
        potentially setting flags

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to calculate the square root of
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `sqrt.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    float_sub(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_sub)
    :   `float_sub` subtracts floating point expression `b` from expression `a` potentially
        setting flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `fsub.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    float_to_int(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_to_int)
    :   `float_to_int` returns integer value of floating point expression `value` of size `size`
        potentially setting flags

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to convert to an int
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `int.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    float_trunc(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.float_trunc)
    :   `float_trunc` rounds a floating point value to an integer towards zero

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to truncate
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `roundint.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    floor(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.floor)
    :   `floor` rounds a floating point value to an integer towards negative infinity

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to round down
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `roundint.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    force_ver(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *dest: architecture.RegisterType*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.force_ver)
    :   `force_ver` creates a new version of the register `dest` Effectively, this is like
        saying r0#2 = r0#1 which MLIL can then use as a new variable definition site.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the register
            - **dest** (*RegisterType*) – the register to force a new version of
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `FORCE_VER(reg)`

        Return type:
        :   ExpressionIndex

    generate_ssa_form() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.generate_ssa_form)
    :   `generate_ssa_form` generate SSA form given the current LLIL

        Return type:
        :   *None*

    get_basic_block_at(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [LowLevelILBasicBlock](#binaryninja.lowlevelil.LowLevelILBasicBlock "binaryninja.lowlevelil.LowLevelILBasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_basic_block_at)
    :   `get_basic_block_at` returns the BasicBlock at the given LLIL instruction `index`.

        Parameters:
        :   **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Index of the LLIL instruction of the BasicBlock to retrieve.

        Example:
        :   ```
            >>> current_il_function.get_basic_block_at(current_il_index)
            <llil block: x86@19-26>
            ```

        Return type:
        :   [*LowLevelILBasicBlock*](#binaryninja.lowlevelil.LowLevelILBasicBlock
            "binaryninja.lowlevelil.LowLevelILBasicBlock") | *None*

    get_exits_for_instr(*idx: InstructionIndex*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[InstructionIndex][[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_exits_for_instr)
    :   Parameters:
        :   **idx** (*InstructionIndex*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[InstructionIndex]

    get_expr(*index: ExpressionIndex*) → [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_expr)
    :   `get_expr` retrieves the IL expression at a given expression index in the function.

        Warning

        Not all IL expressions are valid, even if their index is within the bounds of the
        function, they might not be used by the function and might not contain properly
        structured data.

        Parameters:
        :   **index** (*ExpressionIndex*) – Index of desired expression in function

        Returns:
        :   A LowLevelILInstruction object for the expression, if it exists. Otherwise, None

        Return type:
        :   [*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction") | *None*

    get_expr_count() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_expr_count)
    :   `get_expr_count` gives a the total number of expressions in this IL function

        You can use this to enumerate all expressions in conjunction with
        [`get_expr`](#binaryninja.lowlevelil.LowLevelILFunction.get_expr
        "binaryninja.lowlevelil.LowLevelILFunction.get_expr")

        Warning

        Not all IL expressions are valid, even if their index is within the returned value from
        this, they might not be used by the function and might not contain properly structured
        data.

        Returns:
        :   The number of expressions in the function

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_expr_index_for_instruction(*instr: InstructionIndex*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_expr_index_for_instruction)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   ExpressionIndex

    get_high_level_il_expr_index(*expr: ExpressionIndex*) → ExpressionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_high_level_il_expr_index)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   ExpressionIndex | *None*

    get_high_level_il_instruction_index(*instr: InstructionIndex*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_high_level_il_instruction_index)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   InstructionIndex | *None*

    get_instruction_index_for_expr(*expr: ExpressionIndex*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_instruction_index_for_expr)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   InstructionIndex | *None*

    get_instruction_start(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_instruction_start)
    :   Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –

        Return type:
        :   InstructionIndex | *None*

    get_instructions_at(*addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[InstructionIndex][[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_instructions_at)
    :   `get_instructions_at` gets the InstructionIndex(s) corresponding to the given virtual
        address See the [docs for mappings between
        ils](https://dev-docs.binary.ninja/dev/concepts.html#mapping-between-ils) for more
        information.

        Parameters:
        :   - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – virtual address of the instruction to be queried
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) – (optional) Architecture for the given
              function

        Return type:
        :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")(InstructionIndex)

        Example:
        :   ```
            >>> func = next(bv.functions)
            >>> func.llil.get_instructions_at(func.start)
            [0]
            ```

    get_label_for_address(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*, *addr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [LowLevelILLabel](#binaryninja.lowlevelil.LowLevelILLabel "binaryninja.lowlevelil.LowLevelILLabel") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_label_for_address)
    :   `get_label_for_address` returns the LowLevelILLabel for the given Architecture `arch`
        and IL address `addr` that has been previously added to the function with
        [`add_label_for_address`](#binaryninja.lowlevelil.LowLevelILFunction.add_label_for_address
        "binaryninja.lowlevelil.LowLevelILFunction.add_label_for_address"). When lifting to
        Lifted IL, labels will be automatically added with
        [`add_label_for_address`](#binaryninja.lowlevelil.LowLevelILFunction.add_label_for_address
        "binaryninja.lowlevelil.LowLevelILFunction.add_label_for_address") for the start address
        of every basic block found during disassembly.

        Note

        The returned label is to an internal object with the same lifetime as the containing
        LowLevelILFunction.

        Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture")) –
            - **addr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – IL Address label to retrieve

        Returns:
        :   the LowLevelILLabel for the given IL address

        Return type:
        :   [*LowLevelILLabel*](#binaryninja.lowlevelil.LowLevelILLabel
            "binaryninja.lowlevelil.LowLevelILLabel")

    get_label_for_source_instruction(*i: InstructionIndex*) → [LowLevelILLabel](#binaryninja.lowlevelil.LowLevelILLabel "binaryninja.lowlevelil.LowLevelILLabel") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_label_for_source_instruction)
    :   Get the LowLevelILLabel for a given source instruction. The source instruction must be
        at the start of a basic block in the source function passed to
        [`prepare_to_copy_function`](#binaryninja.lowlevelil.LowLevelILFunction.prepare_to_copy_function
        "binaryninja.lowlevelil.LowLevelILFunction.prepare_to_copy_function"). The label will be
        marked resolved when its source block is passed to
        [`prepare_to_copy_block`](#binaryninja.lowlevelil.LowLevelILFunction.prepare_to_copy_block
        "binaryninja.lowlevelil.LowLevelILFunction.prepare_to_copy_block").

        Warning

        The instruction index parameter for this pertains to the *source function* passed to
        prepare_to_copy_function, not the current function.

        Note

        The returned label is to an internal object with the same lifetime as the containing
        LowLevelILFunction.

        Parameters:
        :   **i** (*InstructionIndex*) – The source instruction index

        Returns:
        :   The LowLevelILLabel for the source instruction

        Return type:
        :   [*LowLevelILLabel*](#binaryninja.lowlevelil.LowLevelILLabel
            "binaryninja.lowlevelil.LowLevelILLabel") | *None*

    get_mapped_medium_level_il_expr_index(*expr: ExpressionIndex*) → ExpressionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_mapped_medium_level_il_expr_index)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   ExpressionIndex | *None*

    get_mapped_medium_level_il_instruction_index(*instr: InstructionIndex*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_mapped_medium_level_il_instruction_index)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   InstructionIndex | *None*

    get_medium_level_il_expr_index(*expr: ExpressionIndex*) → ExpressionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_medium_level_il_expr_index)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   ExpressionIndex | *None*

    get_medium_level_il_expr_indexes(*expr: ExpressionIndex*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex][[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_medium_level_il_expr_indexes)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[ExpressionIndex]

    get_medium_level_il_instruction_index(*instr: InstructionIndex*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_medium_level_il_instruction_index)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   InstructionIndex | *None*

    get_non_ssa_instruction_index(*instr: InstructionIndex*) → InstructionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_non_ssa_instruction_index)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   InstructionIndex

    get_ssa_flag_definition(*flag_ssa: [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")*) → [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_ssa_flag_definition)
    :   Parameters:
        :   **flag_ssa** ([*SSAFlag*](#binaryninja.lowlevelil.SSAFlag
            "binaryninja.lowlevelil.SSAFlag")) –

        Return type:
        :   [*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction") | *None*

    get_ssa_flag_uses(*flag_ssa: [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_ssa_flag_uses)
    :   Parameters:
        :   **flag_ssa** ([*SSAFlag*](#binaryninja.lowlevelil.SSAFlag
            "binaryninja.lowlevelil.SSAFlag")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")]

    get_ssa_flag_value(*flag_ssa: [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_ssa_flag_value)
    :   Parameters:
        :   **flag_ssa** ([*SSAFlag*](#binaryninja.lowlevelil.SSAFlag
            "binaryninja.lowlevelil.SSAFlag")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_ssa_instruction_index(*instr: InstructionIndex*) → InstructionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_ssa_instruction_index)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   InstructionIndex

    get_ssa_memory_definition(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_ssa_memory_definition)
    :   Parameters:
        :   **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction") | *None*

    get_ssa_memory_uses(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_ssa_memory_uses)
    :   Parameters:
        :   **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")]

    get_ssa_reg_definition(*reg_ssa: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*) → [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_ssa_reg_definition)
    :   Parameters:
        :   **reg_ssa** ([*SSARegister*](#binaryninja.lowlevelil.SSARegister
            "binaryninja.lowlevelil.SSARegister")) –

        Return type:
        :   [*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction") | *None*

    get_ssa_reg_uses(*reg_ssa: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_ssa_reg_uses)
    :   Parameters:
        :   **reg_ssa** ([*SSARegister*](#binaryninja.lowlevelil.SSARegister
            "binaryninja.lowlevelil.SSARegister")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")]

    get_ssa_reg_value(*reg_ssa: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.get_ssa_reg_value)
    :   Parameters:
        :   **reg_ssa** ([*SSARegister*](#binaryninja.lowlevelil.SSARegister
            "binaryninja.lowlevelil.SSARegister")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    goto(*label: [LowLevelILLabel](#binaryninja.lowlevelil.LowLevelILLabel "binaryninja.lowlevelil.LowLevelILLabel")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.goto)
    :   `goto` returns a goto expression which jumps to the provided LowLevelILLabel.

        Parameters:
        :   - **label** ([*LowLevelILLabel*](#binaryninja.lowlevelil.LowLevelILLabel
              "binaryninja.lowlevelil.LowLevelILLabel")) – Label to jump to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the ExpressionIndex that jumps to the provided label

        Return type:
        :   ExpressionIndex

    if_expr(*operand: ExpressionIndex*, *t: [LowLevelILLabel](#binaryninja.lowlevelil.LowLevelILLabel "binaryninja.lowlevelil.LowLevelILLabel")*, *f: [LowLevelILLabel](#binaryninja.lowlevelil.LowLevelILLabel "binaryninja.lowlevelil.LowLevelILLabel")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.if_expr)
    :   `if_expr` returns the `if` expression which depending on condition `operand` jumps to
        the LowLevelILLabel `t` when the condition expression `operand` is non-zero and `f` when
        it’s zero.

        Parameters:
        :   - **operand** (*ExpressionIndex*) – comparison expression to evaluate.
            - **t** ([*LowLevelILLabel*](#binaryninja.lowlevelil.LowLevelILLabel
              "binaryninja.lowlevelil.LowLevelILLabel")) – Label for the true branch
            - **f** ([*LowLevelILLabel*](#binaryninja.lowlevelil.LowLevelILLabel
              "binaryninja.lowlevelil.LowLevelILLabel")) – Label for the false branch
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the ExpressionIndex for the if expression

        Return type:
        :   ExpressionIndex

    int_to_float(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.int_to_float)
    :   `int_to_float` returns floating point value of integer expression `value` of size `size`
        potentially setting flags

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to convert to a float
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `float.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    intrinsic(*outputs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [RegisterInfo](architecture.md#binaryninja.architecture.RegisterInfo "binaryninja.architecture.RegisterInfo")]*, *intrinsic: architecture.IntrinsicType*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *flags: architecture.FlagWriteType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.intrinsic)
    :   `intrinsic` return an intrinsic expression.

        Parameters:
        :   - **outputs** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in
              Python v3.14)") *|* [*ILRegister*](#binaryninja.lowlevelil.ILRegister
              "binaryninja.lowlevelil.ILRegister") *|*
              [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|*
              [*ILFlag*](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") *|*
              [*RegisterInfo*](architecture.md#binaryninja.architecture.RegisterInfo
              "binaryninja.architecture.RegisterInfo")*]*) – list of output registers and flags
            - **intrinsic** (*architecture.IntrinsicType*) – name of intrinsic
            - **params** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[**ExpressionIndex**]*) – list of input parameter expressions
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   an intrinsic expression.

        Return type:
        :   ExpressionIndex

    jump(*dest: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.jump)
    :   `jump` returns an expression which jumps (branches) to the expression `dest`

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression to jump to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `jump(dest)`

        Return type:
        :   ExpressionIndex

    jump_to(*dest: ExpressionIndex*, *targets: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [LowLevelILLabel](#binaryninja.lowlevelil.LowLevelILLabel "binaryninja.lowlevelil.LowLevelILLabel")]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.jump_to)
    :   `jump_to` returns an expression which jumps (branches) various targets in `targets`
        choosing the target in `targets` based on the value calculated by `dest`

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression choosing which jump target to use
            - **targets** ([*Dict*](https://docs.python.org/3/library/typing.html#typing.Dict "(in
              Python v3.14)")*[*[*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")*,* [*LowLevelILLabel*](#binaryninja.lowlevelil.LowLevelILLabel
              "binaryninja.lowlevelil.LowLevelILLabel")*]*) – the list of targets for jump locations
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression
            - **targets** –

        Returns:
        :   The expression `jump(dest)`

        Return type:
        :   ExpressionIndex

    load(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *addr: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.load)
    :   `load` Reads `size` bytes from the expression `addr`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to read
            - **addr** (*ExpressionIndex*) – the expression to read memory from
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `[addr].size`

        Return type:
        :   ExpressionIndex

    logical_shift_right(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.logical_shift_right)
    :   `logical_shift_right` shifts logically right expression `a` by expression `b`
        potentially setting flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `lsr.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    low_part(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.low_part)
    :   `low_part` truncates `value` to `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to truncate
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `(value).<size>`

        Return type:
        :   ExpressionIndex

    mark_label(*label: [LowLevelILLabel](#binaryninja.lowlevelil.LowLevelILLabel "binaryninja.lowlevelil.LowLevelILLabel")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.mark_label)
    :   `mark_label` assigns a LowLevelILLabel to the current IL address.

        Parameters:
        :   **label** ([*LowLevelILLabel*](#binaryninja.lowlevelil.LowLevelILLabel
            "binaryninja.lowlevelil.LowLevelILLabel")) –

        Return type:
        :   *None*

    mod_double_prec_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.mod_double_prec_signed)
    :   `mod_double_prec_signed` signed double precision modulus using expression `a` as a
        single double precision register by expression `b` potentially setting flags `flags` and
        returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `mods.dp.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    mod_double_prec_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.mod_double_prec_unsigned)
    :   `mod_double_prec_unsigned` unsigned double precision modulus using expression `a` as a
        single double precision register by expression `b` potentially setting flags `flags` and
        returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `modu.dp.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    mod_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.mod_signed)
    :   `mod_signed` signed modulus expression `a` by expression `b` potentially setting flags
        `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `mods.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    mod_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.mod_unsigned)
    :   `mod_unsigned` unsigned modulus expression `a` by expression `b` potentially setting
        flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `modu.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    mult(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.mult)
    :   `mult` multiplies expression `a` by expression `b` potentially setting flags `flags` and
        returning an expression. Both the operands and return value are `size` bytes as the
        product’s upper half is discarded.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result and input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `mul.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    mult_double_prec_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.mult_double_prec_signed)
    :   `mult_double_prec_signed` multiplies signed with double (2*size bytes) precision
        expression `a` by expression `b`, each `size` bytes and potentially setting flags
        `flags` and returning an expression of `2*size` bytes.

        Note

        The output expression is `2*size` bytes in size, but will be rendered as
        `muls.dp.<size>`.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `muls.dp.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    mult_double_prec_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.mult_double_prec_unsigned)
    :   `mult_double_prec_unsigned` multiplies unsigned with double (2*size bytes) precision
        expression `a` by expression `b`, each `size` bytes and potentially setting flags
        `flags` and returning an expression of `2*size` bytes.

        Note

        The output expression is `2*size` bytes in size, but will be rendered as
        `mulu.dp.<size>`.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the input operands, in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `mulu.dp.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    neg_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.neg_expr)
    :   `neg_expr` two’s complement sign negation of expression `value` of size `size`
        potentially setting flags

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to negate
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `neg.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    no_ret(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.no_ret)
    :   `no_ret` returns an expression that halts disassembly

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `noreturn`

        Return type:
        :   ExpressionIndex

    nop(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.nop)
    :   `nop` no operation, this instruction does nothing

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The no operation expression

        Return type:
        :   ExpressionIndex

    not_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.not_expr)
    :   `not_expr` bitwise inverse of expression `value` of size `size` potentially setting
        flags

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to bitwise invert
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `not.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    operand(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *expr: ExpressionIndex*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.operand)
    :   `operand` sets the operand number of the expression `expr` and passes back `expr`
        without modification.

        Parameters:
        :   - **n** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **expr** (*ExpressionIndex*) –

        Returns:
        :   returns the expression `expr` unmodified

        Return type:
        :   ExpressionIndex

    or_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.or_expr)
    :   `or_expr` bitwise or’s expression `a` and expression `b` potentially setting flags
        `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `or.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    pop(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.pop)
    :   `pop` reads `size` bytes from the stack, adjusting the stack by `size`.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to read from the stack
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `pop`

        Return type:
        :   ExpressionIndex

    prepare_to_copy_block(*src: [LowLevelILBasicBlock](#binaryninja.lowlevelil.LowLevelILBasicBlock "binaryninja.lowlevelil.LowLevelILBasicBlock")*)[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.prepare_to_copy_block)
    :   `prepare_to_copy_block` sets up state when copying a function in preparation of copying
        the instructions from the block `src` It enables use of
        [`get_label_for_source_instruction`](#binaryninja.lowlevelil.LowLevelILFunction.get_label_for_source_instruction
        "binaryninja.lowlevelil.LowLevelILFunction.get_label_for_source_instruction") during
        function transformation.

        Parameters:
        :   **src** ([*LowLevelILBasicBlock*](#binaryninja.lowlevelil.LowLevelILBasicBlock
            "binaryninja.lowlevelil.LowLevelILBasicBlock")) – block about to be copied from

    prepare_to_copy_function(*src: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*)[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.prepare_to_copy_function)
    :   `prepare_to_copy_function` sets up state in this LLIL function in preparation of copying
        instructions from `src`. It enables use of
        [`get_label_for_source_instruction`](#binaryninja.lowlevelil.LowLevelILFunction.get_label_for_source_instruction
        "binaryninja.lowlevelil.LowLevelILFunction.get_label_for_source_instruction") during
        function transformation.

        Parameters:
        :   **src** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
            "binaryninja.lowlevelil.LowLevelILFunction")) – function about to be copied from

    push(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.push)
    :   `push` writes `size` bytes from expression `value` to the stack, adjusting the stack by
        `size`.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to write and adjust the stack by
            - **value** (*ExpressionIndex*) – the expression to write
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression push(value)

        Return type:
        :   ExpressionIndex

    reg(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg: architecture.RegisterType*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.reg)
    :   `reg` returns a register of size `size` with name `reg`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the register in bytes
            - **reg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the name of the register
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   A register expression for the given string

        Return type:
        :   ExpressionIndex

    reg_split(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *hi: architecture.RegisterType*, *lo: architecture.RegisterType*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.reg_split)
    :   `reg_split` combines registers of size `size` with names `hi` and `lo`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the register in bytes
            - **hi** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – register holding high part of value
            - **lo** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – register holding low part of value
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `hi:lo`

        Return type:
        :   ExpressionIndex

    reg_stack_free_reg(*reg: architecture.RegisterType*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.reg_stack_free_reg)
    :   `reg_stack_free_reg` clears the given register `reg` from its register stack without
        affecting the register at the top of the register stack.

        Parameters:
        :   - **reg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the register being marked free
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `__free_slot(reg)`

        Return type:
        :   ExpressionIndex

    reg_stack_free_top_relative(*reg_stack: architecture.RegisterStackType*, *entry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.reg_stack_free_top_relative)
    :   `reg_stack_free_top_relative` clears an entry in the register stack `reg_stack` at a
        top-relative position specified by the value of `entry`.

        Parameters:
        :   - **reg_stack** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the register stack name
            - **entry** (*ExpressionIndex*) – expression to calculate the top-relative position
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `__free_slot(reg_stack[entry])`

        Return type:
        :   ExpressionIndex

    reg_stack_pop(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg_stack: architecture.RegisterStackType*, *flags: architecture.FlagWriteType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.reg_stack_pop)
    :   `reg_stack_pop` returns the top entry of size `size` in register stack with name
        `reg_stack`, and removes the entry from the stack

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the register in bytes
            - **reg_stack** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the name of the register stack
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `reg_stack.pop`

        Return type:
        :   ExpressionIndex

    reg_stack_push(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg_stack: architecture.RegisterStackType*, *value: ExpressionIndex*, *flags: architecture.FlagWriteType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.reg_stack_push)
    :   `reg_stack_push` pushes the expression `value` of size `size` onto the top of the
        register stack `reg_stack`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the register parameter in bytes
            - **reg_stack** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the register stack name
            - **value** (*ExpressionIndex*) – an expression to push
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `reg_stack.push(value)`

        Return type:
        :   ExpressionIndex

    reg_stack_top_relative(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg_stack: architecture.RegisterStackType*, *entry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.reg_stack_top_relative)
    :   `reg_stack_top_relative` returns a register stack entry of size `size` at top-relative
        location `entry` in register stack with name `reg_stack`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the register in bytes
            - **reg_stack** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the name of the register stack
            - **entry** (*ExpressionIndex*) – an expression for which stack entry to fetch
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `reg_stack[entry]`

        Return type:
        :   ExpressionIndex

    replace_expr(*original: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | ExpressionIndex | InstructionIndex*, *new: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | ExpressionIndex | InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.replace_expr)
    :   `replace_expr` allows modification of expressions but ONLY during lifting.

        Warning

        This function should ONLY be called as a part of a lifter or workflow. It will otherwise
        not do anything useful as analysis will not be running.

        Parameters:
        :   - **original** (*ExpressionIndex*) – the ExpressionIndex to replace (may also be an
              expression index)
            - **new** (*ExpressionIndex*) – the ExpressionIndex to add to the current
              LowLevelILFunction (may also be an expression index)

        Return type:
        :   *None*

    ret(*dest: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.ret)
    :   `ret` returns an expression which jumps (branches) to the expression `dest`. `ret` is a
        special alias for jump that makes the disassembler stop disassembling.

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression to jump to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `jump(dest)`

        Return type:
        :   ExpressionIndex

    rotate_left(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.rotate_left)
    :   `rotate_left` bitwise rotates left expression `a` by expression `b` potentially setting
        flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `rol.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    rotate_left_carry(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.rotate_left_carry)
    :   `rotate_left_carry` bitwise rotates left with carry expression `a` by expression `b`
        potentially setting flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **carry** (*ExpressionIndex*) – Carry flag expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `rlc.<size>{<flags>}(a, b, carry)`

        Return type:
        :   ExpressionIndex

    rotate_right(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.rotate_right)
    :   `rotate_right` bitwise rotates right expression `a` by expression `b` potentially
        setting flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `ror.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    rotate_right_carry(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.rotate_right_carry)
    :   `rotate_right_carry` bitwise rotates right with carry expression `a` by expression `b`
        potentially setting flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **carry** (*ExpressionIndex*) – Carry flag expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `rrc.<size>{<flags>}(a, b, carry)`

        Return type:
        :   ExpressionIndex

    round_to_int(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.round_to_int)
    :   `round_to_int` rounds a floating point value to the nearest integer

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to round to the nearest integer
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `roundint.<size>{<flags>}(value)`

        Return type:
        :   ExpressionIndex

    set_current_address(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.set_current_address)
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –

        Return type:
        :   *None*

    set_current_source_block(*block*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.set_current_source_block)
    :   Return type:
        :   *None*

    set_expr_attributes(*expr: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | ExpressionIndex | InstructionIndex*, *value: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ILInstructionAttribute](enums.md#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILInstructionAttribute](enums.md#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute")]*)[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.set_expr_attributes)
    :   `set_expr_attributes` allows modification of instruction attributes but ONLY during
        lifting.

        Warning

        This function should ONLY be called as a part of a lifter or workflow. It will otherwise
        not do anything useful as analysis will not be running.

        Parameters:
        :   - **expr** (*ExpressionIndex*) – the ExpressionIndex to replace (may also be an expression
              index)
            - **value** ([*set*](https://docs.python.org/3/library/stdtypes.html#set "(in Python
              v3.14)")*(*[*ILInstructionAttribute*](enums.md#binaryninja.enums.ILInstructionAttribute
              "binaryninja.enums.ILInstructionAttribute")*)*) – the set of attributes to place on the
              instruction

        Return type:
        :   *None*

    set_flag(*flag: architecture.FlagType*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.set_flag)
    :   `set_flag` sets the flag `flag` to the ExpressionIndex `value`

        Parameters:
        :   - **flag** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the low register name
            - **value** (*ExpressionIndex*) – an expression to set the flag to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression FLAG.flag = value

        Return type:
        :   ExpressionIndex

    set_indirect_branches(*branches: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.set_indirect_branches)
    :   Parameters:
        :   **branches** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple
            "(in Python
            v3.14)")*[*[*Architecture*](architecture.md#binaryninja.architecture.Architecture
            "binaryninja.architecture.Architecture")*,*
            [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*]**]*)
            –

        Return type:
        :   *None*

    set_reg(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg: architecture.RegisterType*, *value: ExpressionIndex*, *flags: architecture.FlagWriteType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.set_reg)
    :   `set_reg` sets the register `reg` of size `size` to the expression `value`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the register parameter in bytes
            - **reg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the register name
            - **value** (*ExpressionIndex*) – an expression to set the register to
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `reg = value`

        Return type:
        :   ExpressionIndex

    set_reg_split(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *hi: architecture.RegisterType*, *lo: architecture.RegisterType*, *value: ExpressionIndex*, *flags: architecture.FlagWriteType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.set_reg_split)
    :   `set_reg_split` uses `hi` and `lo` as a single extended register setting `hi:lo` to the
        expression `value`.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the register parameter in bytes
            - **hi** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the high register name
            - **lo** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the low register name
            - **value** (*ExpressionIndex*) – an expression to set the split registers to
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `hi:lo = value`

        Return type:
        :   ExpressionIndex

    set_reg_stack_top_relative(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *reg_stack: architecture.RegisterStackType*, *entry: ExpressionIndex*, *value: ExpressionIndex*, *flags: architecture.FlagWriteType | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.set_reg_stack_top_relative)
    :   `set_reg_stack_top_relative` sets the top-relative entry `entry` of size `size` in
        register stack `reg_stack` to the expression `value`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the register parameter in bytes
            - **reg_stack** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) – the register stack name
            - **entry** (*ExpressionIndex*) – an expression for which stack entry to set
            - **value** (*ExpressionIndex*) – an expression to set the entry to
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `reg_stack[entry] = value`

        Return type:
        :   ExpressionIndex

    shift_left(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.shift_left)
    :   `shift_left` shifts left expression `a` by expression `b` from expression `a`
        potentially setting flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `lsl.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    sign_extend(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.sign_extend)
    :   `sign_extend` two’s complement sign-extends the expression in `value` to `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to sign extend
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `sx.<size>(value)`

        Return type:
        :   ExpressionIndex

    store(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *addr: ExpressionIndex*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.store)
    :   `store` Writes `size` bytes to expression `addr` read from expression `value`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – number of bytes to write
            - **addr** (*ExpressionIndex*) – the expression to write to
            - **value** (*ExpressionIndex*) – the expression to be written
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `[addr].size = value`

        Return type:
        :   ExpressionIndex

    sub(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.sub)
    :   `sub` subtracts expression `b` from expression `a` potentially setting flags `flags` and
        returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `sub.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    sub_borrow(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.sub_borrow)
    :   `sub_borrow` subtracts with borrow expression `b` from expression `a` potentially
        setting flags `flags` and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **carry** (*ExpressionIndex*) – Carry flag expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `sbb.<size>{<flags>}(a, b, carry)`

        Return type:
        :   ExpressionIndex

    system_call(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.system_call)
    :   `system_call` return a system call expression.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a system call expression.

        Return type:
        :   ExpressionIndex

    tailcall(*dest: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.tailcall)
    :   `tailcall` returns an expression which jumps (branches) to the expression `dest`

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression to jump to
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `tailcall(dest)`

        Return type:
        :   ExpressionIndex

    test_bit(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.test_bit)
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

    translate(*expr_handler: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction"), [LowLevelILBasicBlock](#binaryninja.lowlevelil.LowLevelILBasicBlock "binaryninja.lowlevelil.LowLevelILBasicBlock"), [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")], ExpressionIndex]*) → [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.translate)
    :   `translate` clones an IL function and modifies its expressions as specified by a given
        `expr_handler`, returning the updated IL function.

        Parameters:
        :   **expr_handler**
            ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
            v3.14)")*[**[*[*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
            "binaryninja.lowlevelil.LowLevelILFunction")*,*
            [*LowLevelILBasicBlock*](#binaryninja.lowlevelil.LowLevelILBasicBlock
            "binaryninja.lowlevelil.LowLevelILBasicBlock")*,*
            [*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")*]**,* *ExpressionIndex**]*) –

            Function to modify an expression and copy it to the new function. The function should
            have the following signature:

            expr_handler(new_func: LowLevelILFunction, old_block: LowLevelILBasicBlock, old_instr:
            LowLevelILInstruction) -> ExpressionIndex

            Where:
            :   - **new_func** (*LowLevelILFunction*): New function to receive translated
            instructions
            - **old_block** (*LowLevelILBasicBlock*): Original block containing old_instr
            - **old_instr** (*LowLevelILInstruction*): Original instruction
            - **returns** (*ExpressionIndex*): Expression index of newly created instruction in
            `new_func`

        Returns:
        :   Cloned IL function with modifications

        Return type:
        :   [*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
            "binaryninja.lowlevelil.LowLevelILFunction")

    trap(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.trap)
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

    traverse(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, **args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, ***kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.traverse)
    :   `traverse` iterates through all the instructions in the LowLevelILFunction and calls the
        callback function for each instruction and sub-instruction. See the [Developer
        Docs](https://docs.binary.ninja/dev/concepts.html#walking-ils) for more examples.

        Parameters:
        :   - **cb** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in
              Python
              v3.14)")*[**[*[*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction")*,*
              [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
              v3.14)")*]**,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")*]*) – The callback function to call for each node in the
              LowLevelILInstruction
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

    undefined(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.undefined)
    :   `undefined` returns the undefined expression. This should be used for instructions which
        perform functions but aren’t important for dataflow or partial emulation purposes.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the undefined expression.

        Return type:
        :   ExpressionIndex

    unimplemented(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.unimplemented)
    :   `unimplemented` returns the unimplemented expression. This should be used for all
        instructions which aren’t implemented.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the unimplemented expression.

        Return type:
        :   ExpressionIndex

    unimplemented_memory_ref(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *addr: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.unimplemented_memory_ref)
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

    visit(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.visit)
    :   Iterates over all the instructions in the function and calls the callback function for
        each instruction and each sub-instruction.

        Parameters:
        :   **cb** (*LowLevelILVisitorCallback*) – Callback function that takes the name of the
            operand, the operand, operand type, and parent instruction

        Returns:
        :   True if all instructions were visited, False if the callback function returned False.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`LowLevelILFunction.traverse`](#binaryninja.lowlevelil.LowLevelILFunction.traverse
        "binaryninja.lowlevelil.LowLevelILFunction.traverse") instead.

    visit_all(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.visit_all)
    :   Iterates over all the instructions in the function and calls the callback function for
        each instruction and their operands.

        Parameters:
        :   **cb** (*LowLevelILVisitorCallback*) – Callback function that takes the name of the
            operand, the operand, operand type, and parent instruction

        Returns:
        :   True if all instructions were visited, False if the callback function returned False.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`LowLevelILFunction.traverse`](#binaryninja.lowlevelil.LowLevelILFunction.traverse
        "binaryninja.lowlevelil.LowLevelILFunction.traverse") instead.

    visit_operands(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.visit_operands)
    :   Iterates over all the instructions in the function and calls the callback function for each operand and
        :   the operands of each sub-instruction.

        Parameters:
        :   **cb** (*LowLevelILVisitorCallback*) – Callback function that takes the name of the
            operand, the operand, operand type, and parent instruction

        Returns:
        :   True if all instructions were visited, False if the callback function returned False.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`LowLevelILFunction.traverse`](#binaryninja.lowlevelil.LowLevelILFunction.traverse
        "binaryninja.lowlevelil.LowLevelILFunction.traverse") instead.

    xor_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.xor_expr)
    :   `xor_expr` xor’s expression `a` with expression `b` potentially setting flags `flags`
        and returning an expression of `size` bytes.

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **a** (*ExpressionIndex*) – LHS expression
            - **b** (*ExpressionIndex*) – RHS expression
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `xor.<size>{<flags>}(a, b)`

        Return type:
        :   ExpressionIndex

    zero_extend(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *flags: FlagWriteTypeName | FlagWriteTypeIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILFunction.zero_extend)
    :   `zero_extend` zero-extends the expression in `value` to `size` bytes

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the result in bytes
            - **value** (*ExpressionIndex*) – the expression to zero extend
            - **flags** (*FlagWriteType*) – optional, flag write type caused by this operation
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `zx.<size>(value)`

        Return type:
        :   ExpressionIndex

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    *property* basic_blocks*: [LowLevelILBasicBlockList](function.md#binaryninja.function.LowLevelILBasicBlockList "binaryninja.function.LowLevelILBasicBlockList")*

    *property* current_address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Current IL Address (read/write)

    *property* flags*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")]*
    :   List of flags used in this IL

    *property* il_form*: [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType")*

    *property* instructions*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of llil instructions of the current llil function

    *property* is_thunk*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   Returns True if the function starts with a Tailcall (read-only)

    *property* mapped_medium_level_il*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*
    :   Medium level IL with mappings between low level IL and medium level IL. Unused stores
        are not removed. Typically, this should only be used to answer queries on assembly or
        low level IL where the query is easier to perform on medium level IL.

    *property* medium_level_il*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*
    :   Medium level IL for this low level IL.

    *property* memory_versions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*
    :   List of memory versions used in this IL

    *property* mlil*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    *property* mmlil*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction")*

    *property* non_ssa_form*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*
    :   Low level IL in non-SSA (default) form (read-only)

    *property* reg_stacks*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")]*
    :   List of register stacks used in this IL

    *property* register_stacks*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")]*
    :   Deprecated, use reg_stacks instead. List of register stacks used in this IL

    *property* registers*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*
    :   Deprecated, use regs instead. List of registers used in this IL

    *property* regs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*
    :   List of registers used in this IL

    *property* source_function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* ssa_flags*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")]*
    :   List of all SSA flags and versions used in this IL

    *property* ssa_flags_without_versions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")]*
    :   List of SSA flags used in this IL

    *property* ssa_form*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*
    :   Low level IL in SSA form (read-only)

    *property* ssa_reg_stacks*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")]*
    :   List of all SSA register stacks and versions used in this IL

    *property* ssa_reg_stacks_without_versions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")]*
    :   List of SSA register stacks used in this IL

    *property* ssa_register_stacks*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")]*

    *property* ssa_registers*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*

    *property* ssa_regs*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*
    :   List of all SSA registers and versions used in this IL

    *property* ssa_regs_without_versions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*
    :   List of SSA registers used in this IL

    *property* ssa_vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")]*
    :   This is the union LowLevelILFunction.ssa_regs, LowLevelILFunction.ssa_reg_stacks, and
        LowLevelILFunction.ssa_flags

    *property* ssa_vars_without_versions*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")]*
    :   This is the union LowLevelILFunction.ssa_regs_without_versions,
        LowLevelILFunction.ssa_reg_stacks_without_versions, and
        LowLevelILFunction.ssa_flags_without_versions

    *property* temp_flag_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Number of temporary flags (read-only)

    *property* temp_reg_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Number of temporary registers (read-only)

    *property* vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag")]*
    :   This is the union LowLevelILFunction.regs, LowLevelILFunction.reg_stacks, and
        LowLevelILFunction.flags

    *property* view*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILGoto

*class* LowLevelILGoto[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILGoto)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    LowLevelILGoto(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: InstructionIndex*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILIf

*class* LowLevelILIf[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILIf)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`ControlFlow`](commonil.md#binaryninja.commonil.ControlFlow
    "binaryninja.commonil.ControlFlow")

    LowLevelILIf(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* condition*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    *property* false*: InstructionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* true*: InstructionIndex*

## LowLevelILInstruction

*class* LowLevelILInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction)
:   Bases: [`BaseILInstruction`](commonil.md#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    `class LowLevelILInstruction` Low Level Intermediate Language Instructions are infinite
    length tree-based instructions. Tree-based instructions use infix notation with the left
    hand operand being the destination operand. Infix notation is thus more natural to read
    than other notations (e.g. x86 `mov eax, 0` vs. LLIL `eax = 0`).

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    copy_to(*dest: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *sub_expr_handler: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")], ExpressionIndex] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.copy_to)
    :   `copy_to` deep copies an expression into a new IL function. If provided, the function
        `sub_expr_handler` will be called on every copied sub-expression

        Warning

        This function should ONLY be called as a part of a lifter or workflow. It will otherwise
        not do anything useful as analysis will not be running.

        Parameters:
        :   - **dest** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) – Function to copy the expression to
            - **sub_expr_handler**
              ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python
              v3.14)")*[**[*[*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction")*]**,* *ExpressionIndex**]* *|* *None*) –
              Optional function to call on every copied sub-expression

        Returns:
        :   Index of the copied expression in the target function

        Return type:
        :   ExpressionIndex

    *classmethod* create(*func: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.create)
    :   Parameters:
        :   - **func** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   [*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
            "binaryninja.lowlevelil.LowLevelILInstruction")

    get_flag_value(*flag: architecture.FlagType*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_flag_value)
    :   Parameters:
        :   **flag** (*architecture.FlagType*) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_flag_value_after(*flag: architecture.FlagType*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_flag_value_after)
    :   Parameters:
        :   **flag** (*architecture.FlagType*) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_possible_flag_values(*flag: architecture.FlagType*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_possible_flag_values)
    :   Parameters:
        :   - **flag** (*architecture.FlagType*) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_flag_values_after(*flag: architecture.FlagType*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_possible_flag_values_after)
    :   Parameters:
        :   - **flag** (*architecture.FlagType*) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_reg_values(*reg: architecture.RegisterType*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_possible_reg_values)
    :   Parameters:
        :   - **reg** (*architecture.RegisterType*) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_reg_values_after(*reg: architecture.RegisterType*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_possible_reg_values_after)
    :   Parameters:
        :   - **reg** (*architecture.RegisterType*) –
            - **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
              Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
              "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_possible_stack_contents(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_possible_stack_contents)
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

    get_possible_stack_contents_after(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_possible_stack_contents_after)
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

    get_possible_values(*options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_possible_values)
    :   Parameters:
        :   **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
            "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_reg_value(*reg: architecture.RegisterType*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_reg_value)
    :   Parameters:
        :   **reg** (*architecture.RegisterType*) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_reg_value_after(*reg: architecture.RegisterType*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_reg_value_after)
    :   Parameters:
        :   **reg** (*architecture.RegisterType*) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_stack_contents(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_stack_contents)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    get_stack_contents_after(*offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.get_stack_contents_after)
    :   Parameters:
        :   - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   [*RegisterValue*](variable.md#binaryninja.variable.RegisterValue
            "binaryninja.variable.RegisterValue")

    *static* show_llil_hierarchy()[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.show_llil_hierarchy)
    :   Opens a new tab showing the LLIL hierarchy which includes classes which can easily be
        used with isinstance to match multiple types of IL instructions.

    traverse(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, **args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, ***kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.traverse)
    :   `traverse` is a generator that allows you to traverse the LowLevelILInstruction in a
        depth-first manner. It will yield the result of the callback function for each node in
        the tree. Arguments can be passed to the callback function using `args` and `kwargs`.
        See the [Developer Docs](https://docs.binary.ninja/dev/concepts.html#walking-ils) for
        more examples.

        Parameters:
        :   - **cb** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in
              Python
              v3.14)")*[**[*[*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction")*,*
              [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
              v3.14)")*]**,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")*]*) – The callback function to call for each node in the
              LowLevelILInstruction
            - **args** (*Any*) – Custom user-defined arguments
            - **kwargs** (*Any*) – Custom user-defined keyword arguments
            - **cb** –

        Returns:
        :   An iterator of the results of the callback function

        Return type:
        :   *Iterator*[*Any*]

        Example:
        :   ```
            >>> def get_constant_less_than_value(inst: LowLevelILInstruction, value: int) -> int:
            >>>     if isinstance(inst, Constant) and inst.constant < value:
            >>>         return inst.constant
            >>>
            >>> list(inst.traverse(get_constant_less_than_value, 10))
            ```

    visit(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'root'*, *parent: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.visit)
    :   Visits all LowLevelILInstructions in the operands of this instruction and any
        sub-instructions.

        Parameters:
        :   - **cb** (*LowLevelILVisitorCallback*) – Callback function that takes the name of the
              operand, the operand, operand type, and parent instruction
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **parent** ([*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction") *|* *None*) –

        Returns:
        :   True if all instructions were visited, False if the callback returned False

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`LowLevelILInstruction.traverse`](#binaryninja.lowlevelil.LowLevelILInstruction.traverse
        "binaryninja.lowlevelil.LowLevelILInstruction.traverse") instead.

    visit_all(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'root'*, *parent: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.visit_all)
    :   Visits all operands of this instruction and all operands of any sub-instructions. Using
        pre-order traversal.

        Parameters:
        :   - **cb** (*LowLevelILVisitorCallback*) – Callback function that takes the name of the
              operand, the operand, operand type, and parent instruction
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **parent** ([*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction") *|* *None*) –

        Returns:
        :   True if all instructions were visited, False if the callback returned False

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`LowLevelILInstruction.traverse`](#binaryninja.lowlevelil.LowLevelILInstruction.traverse
        "binaryninja.lowlevelil.LowLevelILInstruction.traverse") instead.

    visit_operands(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'root'*, *parent: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILInstruction.visit_operands)
    :   Visits all leaf operands of this instruction and any sub-instructions.

        Parameters:
        :   - **cb** (*LowLevelILVisitorCallback*) – Callback function that takes the name of the
              operand, the operand, operand type, and parent instruction
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **parent** ([*LowLevelILInstruction*](#binaryninja.lowlevelil.LowLevelILInstruction
              "binaryninja.lowlevelil.LowLevelILInstruction") *|* *None*) –

        Returns:
        :   True if all instructions were visited, False if the callback returned False

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`LowLevelILInstruction.traverse`](#binaryninja.lowlevelil.LowLevelILInstruction.traverse
        "binaryninja.lowlevelil.LowLevelILInstruction.traverse") instead.

    ILOperations*: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar "(in Python v3.14)")[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[LowLevelILOperation](enums.md#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]]]* *= {LowLevelILOperation.LLIL_NOP: [], LowLevelILOperation.LLIL_SET_REG: [('dest', 'reg'), ('src', 'expr')], LowLevelILOperation.LLIL_SET_REG_SPLIT: [('hi', 'reg'), ('lo', 'reg'), ('src', 'expr')], LowLevelILOperation.LLIL_SET_FLAG: [('dest', 'flag'), ('src', 'expr')], LowLevelILOperation.LLIL_SET_REG_STACK_REL: [('stack', 'reg_stack'), ('dest', 'expr'), ('src', 'expr')], LowLevelILOperation.LLIL_REG_STACK_PUSH: [('stack', 'reg_stack'), ('src', 'expr')], LowLevelILOperation.LLIL_LOAD: [('src', 'expr')], LowLevelILOperation.LLIL_STORE: [('dest', 'expr'), ('src', 'expr')], LowLevelILOperation.LLIL_PUSH: [('src', 'expr')], LowLevelILOperation.LLIL_POP: [], LowLevelILOperation.LLIL_REG: [('src', 'reg')], LowLevelILOperation.LLIL_REG_SPLIT: [('hi', 'reg'), ('lo', 'reg')], LowLevelILOperation.LLIL_REG_STACK_REL: [('stack', 'reg_stack'), ('src', 'expr')], LowLevelILOperation.LLIL_REG_STACK_POP: [('stack', 'reg_stack')], LowLevelILOperation.LLIL_REG_STACK_FREE_REG: [('dest', 'reg')], LowLevelILOperation.LLIL_REG_STACK_FREE_REL: [('stack', 'reg_stack'), ('dest', 'expr')], LowLevelILOperation.LLIL_CONST: [('constant', 'int')], LowLevelILOperation.LLIL_CONST_PTR: [('constant', 'int')], LowLevelILOperation.LLIL_EXTERN_PTR: [('constant', 'int'), ('offset', 'int')], LowLevelILOperation.LLIL_FLOAT_CONST: [('constant', 'float')], LowLevelILOperation.LLIL_FLAG: [('src', 'flag')], LowLevelILOperation.LLIL_FLAG_BIT: [('src', 'flag'), ('bit', 'int')], LowLevelILOperation.LLIL_ADD: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_ADC: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], LowLevelILOperation.LLIL_SUB: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_SBB: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], LowLevelILOperation.LLIL_AND: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_OR: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_XOR: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_LSL: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_LSR: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_ASR: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_ROL: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_RLC: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], LowLevelILOperation.LLIL_ROR: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_RRC: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], LowLevelILOperation.LLIL_MUL: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_MULU_DP: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_MULS_DP: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_DIVU: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_DIVU_DP: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_DIVS: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_DIVS_DP: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_MODU: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_MODU_DP: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_MODS: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_MODS_DP: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_NEG: [('src', 'expr')], LowLevelILOperation.LLIL_NOT: [('src', 'expr')], LowLevelILOperation.LLIL_SX: [('src', 'expr')], LowLevelILOperation.LLIL_ZX: [('src', 'expr')], LowLevelILOperation.LLIL_LOW_PART: [('src', 'expr')], LowLevelILOperation.LLIL_JUMP: [('dest', 'expr')], LowLevelILOperation.LLIL_JUMP_TO: [('dest', 'expr'), ('targets', 'target_map')], LowLevelILOperation.LLIL_CALL: [('dest', 'expr')], LowLevelILOperation.LLIL_CALL_STACK_ADJUST: [('dest', 'expr'), ('stack_adjustment', 'int'), ('reg_stack_adjustments', 'reg_stack_adjust')], LowLevelILOperation.LLIL_TAILCALL: [('dest', 'expr')], LowLevelILOperation.LLIL_RET: [('dest', 'expr')], LowLevelILOperation.LLIL_NORET: [], LowLevelILOperation.LLIL_IF: [('condition', 'expr'), ('true', 'int'), ('false', 'int')], LowLevelILOperation.LLIL_GOTO: [('dest', 'int')], LowLevelILOperation.LLIL_FLAG_COND: [('condition', 'cond'), ('semantic_class', 'sem_class')], LowLevelILOperation.LLIL_FLAG_GROUP: [('semantic_group', 'sem_group')], LowLevelILOperation.LLIL_CMP_E: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_CMP_NE: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_CMP_SLT: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_CMP_ULT: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_CMP_SLE: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_CMP_ULE: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_CMP_SGE: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_CMP_UGE: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_CMP_SGT: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_CMP_UGT: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_TEST_BIT: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_BOOL_TO_INT: [('src', 'expr')], LowLevelILOperation.LLIL_ADD_OVERFLOW: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_SYSCALL: [], LowLevelILOperation.LLIL_BP: [], LowLevelILOperation.LLIL_TRAP: [('vector', 'int')], LowLevelILOperation.LLIL_INTRINSIC: [('output', 'reg_or_flag_list'), ('intrinsic', 'intrinsic'), ('param', 'expr')], LowLevelILOperation.LLIL_UNDEF: [], LowLevelILOperation.LLIL_UNIMPL: [], LowLevelILOperation.LLIL_UNIMPL_MEM: [('src', 'expr')], LowLevelILOperation.LLIL_FADD: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FSUB: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FMUL: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FDIV: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FSQRT: [('src', 'expr')], LowLevelILOperation.LLIL_FNEG: [('src', 'expr')], LowLevelILOperation.LLIL_FABS: [('src', 'expr')], LowLevelILOperation.LLIL_FLOAT_TO_INT: [('src', 'expr')], LowLevelILOperation.LLIL_INT_TO_FLOAT: [('src', 'expr')], LowLevelILOperation.LLIL_FLOAT_CONV: [('src', 'expr')], LowLevelILOperation.LLIL_ROUND_TO_INT: [('src', 'expr')], LowLevelILOperation.LLIL_FLOOR: [('src', 'expr')], LowLevelILOperation.LLIL_CEIL: [('src', 'expr')], LowLevelILOperation.LLIL_FTRUNC: [('src', 'expr')], LowLevelILOperation.LLIL_FCMP_E: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FCMP_NE: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FCMP_LT: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FCMP_LE: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FCMP_GE: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FCMP_GT: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FCMP_O: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_FCMP_UO: [('left', 'expr'), ('right', 'expr')], LowLevelILOperation.LLIL_SET_REG_SSA: [('dest', 'reg_ssa'), ('src', 'expr')], LowLevelILOperation.LLIL_SET_REG_SSA_PARTIAL: [('full_reg', 'reg_ssa'), ('dest', 'reg'), ('src', 'expr')], LowLevelILOperation.LLIL_SET_REG_SPLIT_SSA: [('hi', 'expr'), ('lo', 'expr'), ('src', 'expr')], LowLevelILOperation.LLIL_SET_REG_STACK_REL_SSA: [('stack', 'expr'), ('dest', 'expr'), ('top', 'expr'), ('src', 'expr')], LowLevelILOperation.LLIL_SET_REG_STACK_ABS_SSA: [('stack', 'expr'), ('dest', 'reg'), ('src', 'expr')], LowLevelILOperation.LLIL_REG_SPLIT_DEST_SSA: [('dest', 'reg_ssa')], LowLevelILOperation.LLIL_REG_STACK_DEST_SSA: [('src', 'reg_stack_ssa_dest_and_src')], LowLevelILOperation.LLIL_REG_SSA: [('src', 'reg_ssa')], LowLevelILOperation.LLIL_REG_SSA_PARTIAL: [('full_reg', 'reg_ssa'), ('src', 'reg')], LowLevelILOperation.LLIL_REG_SPLIT_SSA: [('hi', 'reg_ssa'), ('lo', 'reg_ssa')], LowLevelILOperation.LLIL_REG_STACK_REL_SSA: [('stack', 'reg_stack_ssa'), ('src', 'expr'), ('top', 'expr')], LowLevelILOperation.LLIL_REG_STACK_ABS_SSA: [('stack', 'reg_stack_ssa'), ('src', 'reg')], LowLevelILOperation.LLIL_REG_STACK_FREE_REL_SSA: [('stack', 'expr'), ('dest', 'expr'), ('top', 'expr')], LowLevelILOperation.LLIL_REG_STACK_FREE_ABS_SSA: [('stack', 'expr'), ('dest', 'reg')], LowLevelILOperation.LLIL_SET_FLAG_SSA: [('dest', 'flag_ssa'), ('src', 'expr')], LowLevelILOperation.LLIL_FLAG_SSA: [('src', 'flag_ssa')], LowLevelILOperation.LLIL_FLAG_BIT_SSA: [('src', 'flag_ssa'), ('bit', 'int')], LowLevelILOperation.LLIL_CALL_SSA: [('output', 'expr'), ('dest', 'expr'), ('stack', 'expr'), ('param', 'expr')], LowLevelILOperation.LLIL_SYSCALL_SSA: [('output', 'expr'), ('stack', 'expr'), ('param', 'expr')], LowLevelILOperation.LLIL_TAILCALL_SSA: [('output', 'expr'), ('dest', 'expr'), ('stack', 'expr'), ('param', 'expr')], LowLevelILOperation.LLIL_CALL_PARAM: [('src', 'expr_list')], LowLevelILOperation.LLIL_CALL_STACK_SSA: [('src', 'reg_ssa'), ('src_memory', 'int')], LowLevelILOperation.LLIL_CALL_OUTPUT_SSA: [('dest_memory', 'int'), ('dest', 'reg_ssa_list')], LowLevelILOperation.LLIL_SEPARATE_PARAM_LIST_SSA: [('src', 'expr_list')], LowLevelILOperation.LLIL_SHARED_PARAM_SLOT_SSA: [('src', 'expr_list')], LowLevelILOperation.LLIL_MEMORY_INTRINSIC_OUTPUT_SSA: [('dest_memory', 'int'), ('output', 'reg_ssa_list')], LowLevelILOperation.LLIL_LOAD_SSA: [('src', 'expr'), ('src_memory', 'int')], LowLevelILOperation.LLIL_STORE_SSA: [('dest', 'expr'), ('dest_memory', 'int'), ('src_memory', 'int'), ('src', 'expr')], LowLevelILOperation.LLIL_INTRINSIC_SSA: [('output', 'reg_or_flag_ssa_list'), ('intrinsic', 'intrinsic'), ('param', 'expr')], LowLevelILOperation.LLIL_MEMORY_INTRINSIC_SSA: [('output', 'expr'), ('intrinsic', 'intrinsic'), ('params', 'expr_list'), ('src_memory', 'int')], LowLevelILOperation.LLIL_REG_PHI: [('dest', 'reg_ssa'), ('src', 'reg_ssa_list')], LowLevelILOperation.LLIL_REG_STACK_PHI: [('dest', 'reg_stack_ssa'), ('src', 'reg_stack_ssa_list')], LowLevelILOperation.LLIL_FLAG_PHI: [('dest', 'flag_ssa'), ('src', 'flag_ssa_list')], LowLevelILOperation.LLIL_MEM_PHI: [('dest_memory', 'int'), ('src_memory', 'int_list')]}*

    *property* address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* attributes*: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ILInstructionAttribute](enums.md#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute")]*
    :   The set of optional attributes placed on the instruction

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    *property* flags*: FlagWriteTypeName | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    *property* high_level_il*: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Gets the high level IL expression corresponding to this expression (may be None for
        eliminated instructions)

    *property* hlil*: [HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* hlils*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](highlevelil.md#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    *property* il_basic_block*: [LowLevelILBasicBlock](#binaryninja.lowlevelil.LowLevelILBasicBlock "binaryninja.lowlevelil.LowLevelILBasicBlock")*
    :   IL basic block object containing this expression (read-only) (only available on
        finalized functions)

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* mapped_medium_level_il*: [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Gets the mapped medium level IL expression corresponding to this expression

    *property* medium_level_il*: [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Gets the medium level IL expression corresponding to this expression (may be None for
        eliminated instructions)

    *property* mlil*: [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* mlils*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")]*

    *property* mmlil*: [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* non_ssa_form*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*
    :   Non-SSA form of expression (read-only)

    *property* operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   Operands for the instruction

        Consider using more specific APIs for `src`, `dest`, `params`, etc where appropriate.

    *property* operation*: [LowLevelILOperation](enums.md#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation")*

    *property* possible_values*: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*
    :   Possible values of expression using path-sensitive static data flow analysis (read-only)

    *property* postfix_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   All operands in the expression tree in postfix order

    *property* prefix_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   All operands in the expression tree in prefix order

    *property* raw_flags*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* raw_operands*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*
    :   Raw operand expression indices as specified by the core structure (read-only)

    *property* size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* source_location*: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation")*

    *property* source_operand*: ExpressionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* ssa_form*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*
    :   SSA form of expression (read-only)

    *property* tokens*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*
    :   LLIL tokens (read-only)

    *property* value*: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*
    :   Value of expression if constant or a known value (read-only)

## LowLevelILIntToFloat

*class* LowLevelILIntToFloat[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILIntToFloat)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILIntToFloat(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILIntrinsic

*class* LowLevelILIntrinsic[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILIntrinsic)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Intrinsic`](commonil.md#binaryninja.commonil.Intrinsic
    "binaryninja.commonil.Intrinsic")

    LowLevelILIntrinsic(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* intrinsic*: [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")]*

    *property* param*: [LowLevelILCallParam](#binaryninja.lowlevelil.LowLevelILCallParam "binaryninja.lowlevelil.LowLevelILCallParam")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

## LowLevelILIntrinsicSsa

*class* LowLevelILIntrinsicSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILIntrinsicSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILIntrinsicSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* intrinsic*: [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")]*

    *property* param*: [LowLevelILCallParam](#binaryninja.lowlevelil.LowLevelILCallParam "binaryninja.lowlevelil.LowLevelILCallParam")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

## LowLevelILJump

*class* LowLevelILJump[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILJump)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    LowLevelILJump(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILJumpTo

*class* LowLevelILJumpTo[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILJumpTo)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILJumpTo(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* targets*: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

## LowLevelILLabel

*class* LowLevelILLabel[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILLabel)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    __init__(*handle: BNLowLevelILLabel | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILLabel.__init__)
    :   Parameters:
        :   **handle** (*BNLowLevelILLabel* *|* *None*) –

    *property* operand*: InstructionIndex*

    *property* ref*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* resolved*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

## LowLevelILLoad

*class* LowLevelILLoad[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILLoad)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Load`](commonil.md#binaryninja.commonil.Load "binaryninja.commonil.Load")

    LowLevelILLoad(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILLoadSsa

*class* LowLevelILLoadSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILLoadSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Load`](commonil.md#binaryninja.commonil.Load "binaryninja.commonil.Load"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILLoadSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LowLevelILLowPart

*class* LowLevelILLowPart[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILLowPart)
:   Bases: [`LowLevelILUnaryBase`](#binaryninja.lowlevelil.LowLevelILUnaryBase
    "binaryninja.lowlevelil.LowLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILLowPart(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILLsl

*class* LowLevelILLsl[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILLsl)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILLsl(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILLsr

*class* LowLevelILLsr[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILLsr)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILLsr(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILMemPhi

*class* LowLevelILMemPhi[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILMemPhi)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Memory`](commonil.md#binaryninja.commonil.Memory "binaryninja.commonil.Memory"),
    [`Phi`](commonil.md#binaryninja.commonil.Phi "binaryninja.commonil.Phi")

    LowLevelILMemPhi(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src_memory*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

## LowLevelILMemoryIntrinsicOutputSsa

*class* LowLevelILMemoryIntrinsicOutputSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILMemoryIntrinsicOutputSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILMemoryIntrinsicOutputSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")]*

## LowLevelILMemoryIntrinsicSsa

*class* LowLevelILMemoryIntrinsicSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILMemoryIntrinsicSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILMemoryIntrinsicSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* intrinsic*: [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")]*

    *property* param*: [LowLevelILCallParam](#binaryninja.lowlevelil.LowLevelILCallParam "binaryninja.lowlevelil.LowLevelILCallParam")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LowLevelILMods

*class* LowLevelILMods[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILMods)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"), [`Signed`](commonil.md#binaryninja.commonil.Signed
    "binaryninja.commonil.Signed")

    LowLevelILMods(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILModsDp

*class* LowLevelILModsDp[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILModsDp)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    LowLevelILModsDp(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILModu

*class* LowLevelILModu[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILModu)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILModu(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILModuDp

*class* LowLevelILModuDp[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILModuDp)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    LowLevelILModuDp(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILMul

*class* LowLevelILMul[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILMul)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILMul(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILMulsDp

*class* LowLevelILMulsDp[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILMulsDp)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    LowLevelILMulsDp(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILMuluDp

*class* LowLevelILMuluDp[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILMuluDp)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    LowLevelILMuluDp(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILNeg

*class* LowLevelILNeg[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILNeg)
:   Bases: [`LowLevelILUnaryBase`](#binaryninja.lowlevelil.LowLevelILUnaryBase
    "binaryninja.lowlevelil.LowLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILNeg(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILNop

*class* LowLevelILNop[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILNop)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILNop(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILNoret

*class* LowLevelILNoret[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILNoret)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    LowLevelILNoret(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILNot

*class* LowLevelILNot[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILNot)
:   Bases: [`LowLevelILUnaryBase`](#binaryninja.lowlevelil.LowLevelILUnaryBase
    "binaryninja.lowlevelil.LowLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILNot(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILOperationAndSize

*class* LowLevelILOperationAndSize[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILOperationAndSize)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    LowLevelILOperationAndSize(operation: ‘LowLevelILOperation’, size: int)

    __init__(*operation: [LowLevelILOperation](enums.md#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **operation** ([*LowLevelILOperation*](enums.md#binaryninja.enums.LowLevelILOperation
              "binaryninja.enums.LowLevelILOperation")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    operation*: [LowLevelILOperation](enums.md#binaryninja.enums.LowLevelILOperation "binaryninja.enums.LowLevelILOperation")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LowLevelILOr

*class* LowLevelILOr[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILOr)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILOr(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILPop

*class* LowLevelILPop[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILPop)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`StackOperation`](commonil.md#binaryninja.commonil.StackOperation
    "binaryninja.commonil.StackOperation")

    LowLevelILPop(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILPush

*class* LowLevelILPush[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILPush)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`StackOperation`](commonil.md#binaryninja.commonil.StackOperation
    "binaryninja.commonil.StackOperation")

    LowLevelILPush(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILReg

*class* LowLevelILReg[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILReg)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILReg(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

## LowLevelILRegPhi

*class* LowLevelILRegPhi[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegPhi)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Phi`](commonil.md#binaryninja.commonil.Phi "binaryninja.commonil.Phi")

    LowLevelILRegPhi(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*

## LowLevelILRegSplit

*class* LowLevelILRegSplit[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegSplit)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILRegSplit(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    *property* hi*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* lo*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

## LowLevelILRegSplitDestSsa

*class* LowLevelILRegSplitDestSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegSplitDestSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILRegSplitDestSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILRegSplitSsa

*class* LowLevelILRegSplitSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegSplitSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SetReg`](commonil.md#binaryninja.commonil.SetReg "binaryninja.commonil.SetReg"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILRegSplitSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    *property* hi*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* lo*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

## LowLevelILRegSsa

*class* LowLevelILRegSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILRegSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

## LowLevelILRegSsaPartial

*class* LowLevelILRegSsaPartial[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegSsaPartial)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SetReg`](commonil.md#binaryninja.commonil.SetReg "binaryninja.commonil.SetReg"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILRegSsaPartial(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    *property* full_reg*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

## LowLevelILRegStackAbsSsa

*class* LowLevelILRegStackAbsSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackAbsSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    LowLevelILRegStackAbsSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    *property* stack*: [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")*

## LowLevelILRegStackDestSsa

*class* LowLevelILRegStackDestSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackDestSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    LowLevelILRegStackDestSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")*

## LowLevelILRegStackFreeAbsSsa

*class* LowLevelILRegStackFreeAbsSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackFreeAbsSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack")

    LowLevelILRegStackFreeAbsSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* stack*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILRegStackFreeReg

*class* LowLevelILRegStackFreeReg[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackFreeReg)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack")

    LowLevelILRegStackFreeReg(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILRegStackFreeRel

*class* LowLevelILRegStackFreeRel[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackFreeRel)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack")

    LowLevelILRegStackFreeRel(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* stack*: [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack")*

## LowLevelILRegStackFreeRelSsa

*class* LowLevelILRegStackFreeRelSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackFreeRelSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    LowLevelILRegStackFreeRelSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* stack*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* top*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILRegStackPhi

*class* LowLevelILRegStackPhi[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackPhi)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack"), [`Phi`](commonil.md#binaryninja.commonil.Phi
    "binaryninja.commonil.Phi")

    LowLevelILRegStackPhi(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")]*

## LowLevelILRegStackPop

*class* LowLevelILRegStackPop[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackPop)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack")

    LowLevelILRegStackPop(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* stack*: [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack")*

## LowLevelILRegStackPush

*class* LowLevelILRegStackPush[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackPush)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack")

    LowLevelILRegStackPush(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* stack*: [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack")*

## LowLevelILRegStackRel

*class* LowLevelILRegStackRel[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackRel)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack")

    LowLevelILRegStackRel(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* stack*: [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack")*

## LowLevelILRegStackRelSsa

*class* LowLevelILRegStackRelSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRegStackRelSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    LowLevelILRegStackRelSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* stack*: [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")*

    *property* top*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILRet

*class* LowLevelILRet[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRet)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Return`](commonil.md#binaryninja.commonil.Return "binaryninja.commonil.Return")

    LowLevelILRet(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILRlc

*class* LowLevelILRlc[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRlc)
:   Bases: [`LowLevelILCarryBase`](#binaryninja.lowlevelil.LowLevelILCarryBase
    "binaryninja.lowlevelil.LowLevelILCarryBase")

    LowLevelILRlc(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILRol

*class* LowLevelILRol[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRol)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILRol(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILRor

*class* LowLevelILRor[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRor)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILRor(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILRoundToInt

*class* LowLevelILRoundToInt[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRoundToInt)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILRoundToInt(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILRrc

*class* LowLevelILRrc[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILRrc)
:   Bases: [`LowLevelILCarryBase`](#binaryninja.lowlevelil.LowLevelILCarryBase
    "binaryninja.lowlevelil.LowLevelILCarryBase")

    LowLevelILRrc(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILSbb

*class* LowLevelILSbb[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSbb)
:   Bases: [`LowLevelILCarryBase`](#binaryninja.lowlevelil.LowLevelILCarryBase
    "binaryninja.lowlevelil.LowLevelILCarryBase")

    LowLevelILSbb(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILSeparateParamListSsa

*class* LowLevelILSeparateParamListSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSeparateParamListSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILSeparateParamListSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

## LowLevelILSetFlag

*class* LowLevelILSetFlag[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetFlag)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILSetFlag(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILSetFlagSsa

*class* LowLevelILSetFlagSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetFlagSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILSetFlagSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILSetReg

*class* LowLevelILSetReg[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetReg)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SetReg`](commonil.md#binaryninja.commonil.SetReg "binaryninja.commonil.SetReg")

    LowLevelILSetReg(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILSetRegSplit

*class* LowLevelILSetRegSplit[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetRegSplit)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SetReg`](commonil.md#binaryninja.commonil.SetReg "binaryninja.commonil.SetReg")

    LowLevelILSetRegSplit(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    *property* hi*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* lo*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILSetRegSplitSsa

*class* LowLevelILSetRegSplitSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetRegSplitSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SetReg`](commonil.md#binaryninja.commonil.SetReg "binaryninja.commonil.SetReg"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILSetRegSplitSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    *property* hi*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* lo*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILSetRegSsa

*class* LowLevelILSetRegSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetRegSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SetReg`](commonil.md#binaryninja.commonil.SetReg "binaryninja.commonil.SetReg"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILSetRegSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILSetRegSsaPartial

*class* LowLevelILSetRegSsaPartial[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetRegSsaPartial)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SetReg`](commonil.md#binaryninja.commonil.SetReg "binaryninja.commonil.SetReg"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILSetRegSsaPartial(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    *property* full_reg*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILSetRegStackAbsSsa

*class* LowLevelILSetRegStackAbsSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetRegStackAbsSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    LowLevelILSetRegStackAbsSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* stack*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILSetRegStackRel

*class* LowLevelILSetRegStackRel[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetRegStackRel)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack")

    LowLevelILSetRegStackRel(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* stack*: [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack")*

## LowLevelILSetRegStackRelSsa

*class* LowLevelILSetRegStackRelSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSetRegStackRelSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`RegisterStack`](commonil.md#binaryninja.commonil.RegisterStack
    "binaryninja.commonil.RegisterStack"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    LowLevelILSetRegStackRelSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* stack*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* top*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILSharedParamSlotSsa

*class* LowLevelILSharedParamSlotSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSharedParamSlotSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILSharedParamSlotSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

## LowLevelILStore

*class* LowLevelILStore[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILStore)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Store`](commonil.md#binaryninja.commonil.Store "binaryninja.commonil.Store")

    LowLevelILStore(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILStoreSsa

*class* LowLevelILStoreSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILStoreSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Store`](commonil.md#binaryninja.commonil.Store "binaryninja.commonil.Store"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILStoreSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LowLevelILSub

*class* LowLevelILSub[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSub)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILSub(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILSx

*class* LowLevelILSx[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSx)
:   Bases: [`LowLevelILUnaryBase`](#binaryninja.lowlevelil.LowLevelILUnaryBase
    "binaryninja.lowlevelil.LowLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILSx(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILSyscall

*class* LowLevelILSyscall[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSyscall)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Syscall`](commonil.md#binaryninja.commonil.Syscall "binaryninja.commonil.Syscall")

    LowLevelILSyscall(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILSyscallSsa

*class* LowLevelILSyscallSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILSyscallSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Syscall`](commonil.md#binaryninja.commonil.Syscall "binaryninja.commonil.Syscall"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    LowLevelILSyscallSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*

    *property* param*: [LowLevelILCallParam](#binaryninja.lowlevelil.LowLevelILCallParam "binaryninja.lowlevelil.LowLevelILCallParam")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

    *property* stack*: [LowLevelILCallStackSsa](#binaryninja.lowlevelil.LowLevelILCallStackSsa "binaryninja.lowlevelil.LowLevelILCallStackSsa")*

    *property* stack_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* stack_reg*: [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")*

## LowLevelILTailcall

*class* LowLevelILTailcall[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILTailcall)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Tailcall`](commonil.md#binaryninja.commonil.Tailcall "binaryninja.commonil.Tailcall")

    LowLevelILTailcall(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILTailcallSsa

*class* LowLevelILTailcallSsa[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILTailcallSsa)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Tailcall`](commonil.md#binaryninja.commonil.Tailcall "binaryninja.commonil.Tailcall"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    LowLevelILTailcallSsa(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* dest*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* output*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")]*

    *property* param*: [LowLevelILCallParam](#binaryninja.lowlevelil.LowLevelILCallParam "binaryninja.lowlevelil.LowLevelILCallParam")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")]*

    *property* stack*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILTestBit

*class* LowLevelILTestBit[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILTestBit)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    LowLevelILTestBit(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILTrap

*class* LowLevelILTrap[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILTrap)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    LowLevelILTrap(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* vector*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LowLevelILUnaryBase

*class* LowLevelILUnaryBase[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILUnaryBase)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`UnaryOperation`](commonil.md#binaryninja.commonil.UnaryOperation
    "binaryninja.commonil.UnaryOperation")

    LowLevelILUnaryBase(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILUndef

*class* LowLevelILUndef[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILUndef)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    LowLevelILUndef(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILUnimpl

*class* LowLevelILUnimpl[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILUnimpl)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction")

    LowLevelILUnimpl(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILUnimplMem

*class* LowLevelILUnimplMem[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILUnimplMem)
:   Bases: [`LowLevelILInstruction`](#binaryninja.lowlevelil.LowLevelILInstruction
    "binaryninja.lowlevelil.LowLevelILInstruction"),
    [`Memory`](commonil.md#binaryninja.commonil.Memory "binaryninja.commonil.Memory")

    LowLevelILUnimplMem(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [LowLevelILOperationAndSize](#binaryninja.lowlevelil.LowLevelILOperationAndSize "binaryninja.lowlevelil.LowLevelILOperationAndSize") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILIntrinsic](#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[RegisterStackName, [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag") | [SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister") | [SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack") | [ILSemanticFlagClass](#binaryninja.lowlevelil.ILSemanticFlagClass "binaryninja.lowlevelil.ILSemanticFlagClass") | [ILSemanticFlagGroup](#binaryninja.lowlevelil.ILSemanticFlagGroup "binaryninja.lowlevelil.ILSemanticFlagGroup") | [LowLevelILFlagCondition](enums.md#binaryninja.enums.LowLevelILFlagCondition "binaryninja.enums.LowLevelILFlagCondition") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag") | [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegister](#binaryninja.lowlevelil.SSARegister "binaryninja.lowlevelil.SSARegister")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterStack](#binaryninja.lowlevelil.SSARegisterStack "binaryninja.lowlevelil.SSARegisterStack")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAFlag](#binaryninja.lowlevelil.SSAFlag "binaryninja.lowlevelil.SSAFlag")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSARegisterOrFlag](#binaryninja.lowlevelil.SSARegisterOrFlag "binaryninja.lowlevelil.SSARegisterOrFlag")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* src*: [LowLevelILInstruction](#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction")*

## LowLevelILXor

*class* LowLevelILXor[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILXor)
:   Bases: [`LowLevelILBinaryBase`](#binaryninja.lowlevelil.LowLevelILBinaryBase
    "binaryninja.lowlevelil.LowLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILXor(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## LowLevelILZx

*class* LowLevelILZx[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LowLevelILZx)
:   Bases: [`LowLevelILUnaryBase`](#binaryninja.lowlevelil.LowLevelILUnaryBase
    "binaryninja.lowlevelil.LowLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    LowLevelILZx(function: ‘LowLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x10a719790>, instr:
    binaryninja.lowlevelil.CoreLowLevelILInstruction, instr_index:
    Optional[InstructionIndex])

    __init__(*function: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*, *expr_index: ExpressionIndex*, *instr: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*LowLevelILFunction*](#binaryninja.lowlevelil.LowLevelILFunction
              "binaryninja.lowlevelil.LowLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **instr**
              ([*CoreLowLevelILInstruction*](#binaryninja.lowlevelil.CoreLowLevelILInstruction
              "binaryninja.lowlevelil.CoreLowLevelILInstruction")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   *None*

    expr_index*: ExpressionIndex*

    function*: [LowLevelILFunction](#binaryninja.lowlevelil.LowLevelILFunction "binaryninja.lowlevelil.LowLevelILFunction")*

    instr*: [CoreLowLevelILInstruction](#binaryninja.lowlevelil.CoreLowLevelILInstruction "binaryninja.lowlevelil.CoreLowLevelILInstruction")*

    instr_index*: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## SSAFlag

*class* SSAFlag[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#SSAFlag)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    SSAFlag(flag: binaryninja.lowlevelil.ILFlag, version: int)

    __init__(*flag: [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag")*, *version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **flag** ([*ILFlag*](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag")) –
            - **version** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    flag*: [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag")*

    version*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## SSARegister

*class* SSARegister[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#SSARegister)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    SSARegister(reg: binaryninja.lowlevelil.ILRegister, version: int)

    __init__(*reg: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*, *version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **reg** ([*ILRegister*](#binaryninja.lowlevelil.ILRegister
              "binaryninja.lowlevelil.ILRegister")) –
            - **version** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    reg*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister")*

    version*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## SSARegisterOrFlag

*class* SSARegisterOrFlag[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#SSARegisterOrFlag)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    SSARegisterOrFlag(reg_or_flag: Union[binaryninja.lowlevelil.ILRegister,
    binaryninja.lowlevelil.ILFlag], version: int)

    __init__(*reg_or_flag: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag")*, *version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **reg_or_flag** ([*ILRegister*](#binaryninja.lowlevelil.ILRegister
              "binaryninja.lowlevelil.ILRegister") *|* [*ILFlag*](#binaryninja.lowlevelil.ILFlag
              "binaryninja.lowlevelil.ILFlag")) –
            - **version** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    reg_or_flag*: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [ILFlag](#binaryninja.lowlevelil.ILFlag "binaryninja.lowlevelil.ILFlag")*

    version*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## SSARegisterStack

*class* SSARegisterStack[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#SSARegisterStack)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    SSARegisterStack(reg_stack: binaryninja.lowlevelil.ILRegisterStack, version: int)

    __init__(*reg_stack: [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack")*, *version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **reg_stack** ([*ILRegisterStack*](#binaryninja.lowlevelil.ILRegisterStack
              "binaryninja.lowlevelil.ILRegisterStack")) –
            - **version** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    reg_stack*: [ILRegisterStack](#binaryninja.lowlevelil.ILRegisterStack "binaryninja.lowlevelil.ILRegisterStack")*

    version*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## LLIL_GET_TEMP_REG_INDEX

LLIL_GET_TEMP_REG_INDEX(*n: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LLIL_GET_TEMP_REG_INDEX)
:   Parameters:
    :   **n** ([*ILRegister*](#binaryninja.lowlevelil.ILRegister
        "binaryninja.lowlevelil.ILRegister") *|*
        [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) –

    Return type:
    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

## LLIL_REG_IS_TEMP

LLIL_REG_IS_TEMP(*n: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LLIL_REG_IS_TEMP)
:   Parameters:
    :   **n** ([*ILRegister*](#binaryninja.lowlevelil.ILRegister
        "binaryninja.lowlevelil.ILRegister") *|*
        [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) –

    Return type:
    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

## LLIL_TEMP

LLIL_TEMP(*n: [ILRegister](#binaryninja.lowlevelil.ILRegister "binaryninja.lowlevelil.ILRegister") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → RegisterIndex[[source]](https://api.binary.ninja/_modules/binaryninja/lowlevelil.html#LLIL_TEMP)
:   Parameters:
    :   **n** ([*ILRegister*](#binaryninja.lowlevelil.ILRegister
        "binaryninja.lowlevelil.ILRegister") *|*
        [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) –

    Return type:
    :   RegisterIndex
