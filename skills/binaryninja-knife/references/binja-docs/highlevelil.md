# highlevelil module

| Class | Description |
| --- | --- |
| [`binaryninja.highlevelil.CoreHighLevelILInstruction`](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction") |  |
| [`binaryninja.highlevelil.GotoLabel`](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") |  |
| [`binaryninja.highlevelil.HighLevelILAdc`](#binaryninja.highlevelil.HighLevelILAdc "binaryninja.highlevelil.HighLevelILAdc") |  |
| [`binaryninja.highlevelil.HighLevelILAdd`](#binaryninja.highlevelil.HighLevelILAdd "binaryninja.highlevelil.HighLevelILAdd") |  |
| [`binaryninja.highlevelil.HighLevelILAddOverflow`](#binaryninja.highlevelil.HighLevelILAddOverflow "binaryninja.highlevelil.HighLevelILAddOverflow") |  |
| [`binaryninja.highlevelil.HighLevelILAddressOf`](#binaryninja.highlevelil.HighLevelILAddressOf "binaryninja.highlevelil.HighLevelILAddressOf") |  |
| [`binaryninja.highlevelil.HighLevelILAnd`](#binaryninja.highlevelil.HighLevelILAnd "binaryninja.highlevelil.HighLevelILAnd") |  |
| [`binaryninja.highlevelil.HighLevelILArrayIndex`](#binaryninja.highlevelil.HighLevelILArrayIndex "binaryninja.highlevelil.HighLevelILArrayIndex") |  |
| [`binaryninja.highlevelil.HighLevelILArrayIndexSsa`](#binaryninja.highlevelil.HighLevelILArrayIndexSsa "binaryninja.highlevelil.HighLevelILArrayIndexSsa") |  |
| [`binaryninja.highlevelil.HighLevelILAsr`](#binaryninja.highlevelil.HighLevelILAsr "binaryninja.highlevelil.HighLevelILAsr") |  |
| [`binaryninja.highlevelil.HighLevelILAssert`](#binaryninja.highlevelil.HighLevelILAssert "binaryninja.highlevelil.HighLevelILAssert") |  |
| [`binaryninja.highlevelil.HighLevelILAssertSsa`](#binaryninja.highlevelil.HighLevelILAssertSsa "binaryninja.highlevelil.HighLevelILAssertSsa") |  |
| [`binaryninja.highlevelil.HighLevelILAssign`](#binaryninja.highlevelil.HighLevelILAssign "binaryninja.highlevelil.HighLevelILAssign") |  |
| [`binaryninja.highlevelil.HighLevelILAssignMemSsa`](#binaryninja.highlevelil.HighLevelILAssignMemSsa "binaryninja.highlevelil.HighLevelILAssignMemSsa") |  |
| [`binaryninja.highlevelil.HighLevelILAssignUnpack`](#binaryninja.highlevelil.HighLevelILAssignUnpack "binaryninja.highlevelil.HighLevelILAssignUnpack") |  |
| [`binaryninja.highlevelil.HighLevelILAssignUnpackMemSsa`](#binaryninja.highlevelil.HighLevelILAssignUnpackMemSsa "binaryninja.highlevelil.HighLevelILAssignUnpackMemSsa") |  |
| [`binaryninja.highlevelil.HighLevelILBasicBlock`](#binaryninja.highlevelil.HighLevelILBasicBlock "binaryninja.highlevelil.HighLevelILBasicBlock") | The `HighLevelILBasicBlock` object is returned during analysis and should not be directly… |
| [`binaryninja.highlevelil.HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase "binaryninja.highlevelil.HighLevelILBinaryBase") |  |
| [`binaryninja.highlevelil.HighLevelILBlock`](#binaryninja.highlevelil.HighLevelILBlock "binaryninja.highlevelil.HighLevelILBlock") |  |
| [`binaryninja.highlevelil.HighLevelILBoolToInt`](#binaryninja.highlevelil.HighLevelILBoolToInt "binaryninja.highlevelil.HighLevelILBoolToInt") |  |
| [`binaryninja.highlevelil.HighLevelILBp`](#binaryninja.highlevelil.HighLevelILBp "binaryninja.highlevelil.HighLevelILBp") |  |
| [`binaryninja.highlevelil.HighLevelILBreak`](#binaryninja.highlevelil.HighLevelILBreak "binaryninja.highlevelil.HighLevelILBreak") |  |
| [`binaryninja.highlevelil.HighLevelILCall`](#binaryninja.highlevelil.HighLevelILCall "binaryninja.highlevelil.HighLevelILCall") |  |
| [`binaryninja.highlevelil.HighLevelILCallSsa`](#binaryninja.highlevelil.HighLevelILCallSsa "binaryninja.highlevelil.HighLevelILCallSsa") |  |
| [`binaryninja.highlevelil.HighLevelILCarryBase`](#binaryninja.highlevelil.HighLevelILCarryBase "binaryninja.highlevelil.HighLevelILCarryBase") |  |
| [`binaryninja.highlevelil.HighLevelILCase`](#binaryninja.highlevelil.HighLevelILCase "binaryninja.highlevelil.HighLevelILCase") |  |
| [`binaryninja.highlevelil.HighLevelILCeil`](#binaryninja.highlevelil.HighLevelILCeil "binaryninja.highlevelil.HighLevelILCeil") |  |
| [`binaryninja.highlevelil.HighLevelILCmpE`](#binaryninja.highlevelil.HighLevelILCmpE "binaryninja.highlevelil.HighLevelILCmpE") |  |
| [`binaryninja.highlevelil.HighLevelILCmpNe`](#binaryninja.highlevelil.HighLevelILCmpNe "binaryninja.highlevelil.HighLevelILCmpNe") |  |
| [`binaryninja.highlevelil.HighLevelILCmpSge`](#binaryninja.highlevelil.HighLevelILCmpSge "binaryninja.highlevelil.HighLevelILCmpSge") |  |
| [`binaryninja.highlevelil.HighLevelILCmpSgt`](#binaryninja.highlevelil.HighLevelILCmpSgt "binaryninja.highlevelil.HighLevelILCmpSgt") |  |
| [`binaryninja.highlevelil.HighLevelILCmpSle`](#binaryninja.highlevelil.HighLevelILCmpSle "binaryninja.highlevelil.HighLevelILCmpSle") |  |
| [`binaryninja.highlevelil.HighLevelILCmpSlt`](#binaryninja.highlevelil.HighLevelILCmpSlt "binaryninja.highlevelil.HighLevelILCmpSlt") |  |
| [`binaryninja.highlevelil.HighLevelILCmpUge`](#binaryninja.highlevelil.HighLevelILCmpUge "binaryninja.highlevelil.HighLevelILCmpUge") |  |
| [`binaryninja.highlevelil.HighLevelILCmpUgt`](#binaryninja.highlevelil.HighLevelILCmpUgt "binaryninja.highlevelil.HighLevelILCmpUgt") |  |
| [`binaryninja.highlevelil.HighLevelILCmpUle`](#binaryninja.highlevelil.HighLevelILCmpUle "binaryninja.highlevelil.HighLevelILCmpUle") |  |
| [`binaryninja.highlevelil.HighLevelILCmpUlt`](#binaryninja.highlevelil.HighLevelILCmpUlt "binaryninja.highlevelil.HighLevelILCmpUlt") |  |
| [`binaryninja.highlevelil.HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase "binaryninja.highlevelil.HighLevelILComparisonBase") |  |
| [`binaryninja.highlevelil.HighLevelILConst`](#binaryninja.highlevelil.HighLevelILConst "binaryninja.highlevelil.HighLevelILConst") |  |
| [`binaryninja.highlevelil.HighLevelILConstData`](#binaryninja.highlevelil.HighLevelILConstData "binaryninja.highlevelil.HighLevelILConstData") |  |
| [`binaryninja.highlevelil.HighLevelILConstPtr`](#binaryninja.highlevelil.HighLevelILConstPtr "binaryninja.highlevelil.HighLevelILConstPtr") |  |
| [`binaryninja.highlevelil.HighLevelILContinue`](#binaryninja.highlevelil.HighLevelILContinue "binaryninja.highlevelil.HighLevelILContinue") |  |
| [`binaryninja.highlevelil.HighLevelILDeref`](#binaryninja.highlevelil.HighLevelILDeref "binaryninja.highlevelil.HighLevelILDeref") |  |
| [`binaryninja.highlevelil.HighLevelILDerefField`](#binaryninja.highlevelil.HighLevelILDerefField "binaryninja.highlevelil.HighLevelILDerefField") |  |
| [`binaryninja.highlevelil.HighLevelILDerefFieldSsa`](#binaryninja.highlevelil.HighLevelILDerefFieldSsa "binaryninja.highlevelil.HighLevelILDerefFieldSsa") |  |
| [`binaryninja.highlevelil.HighLevelILDerefSsa`](#binaryninja.highlevelil.HighLevelILDerefSsa "binaryninja.highlevelil.HighLevelILDerefSsa") |  |
| [`binaryninja.highlevelil.HighLevelILDivs`](#binaryninja.highlevelil.HighLevelILDivs "binaryninja.highlevelil.HighLevelILDivs") |  |
| [`binaryninja.highlevelil.HighLevelILDivsDp`](#binaryninja.highlevelil.HighLevelILDivsDp "binaryninja.highlevelil.HighLevelILDivsDp") |  |
| [`binaryninja.highlevelil.HighLevelILDivu`](#binaryninja.highlevelil.HighLevelILDivu "binaryninja.highlevelil.HighLevelILDivu") |  |
| [`binaryninja.highlevelil.HighLevelILDivuDp`](#binaryninja.highlevelil.HighLevelILDivuDp "binaryninja.highlevelil.HighLevelILDivuDp") |  |
| [`binaryninja.highlevelil.HighLevelILDoWhile`](#binaryninja.highlevelil.HighLevelILDoWhile "binaryninja.highlevelil.HighLevelILDoWhile") |  |
| [`binaryninja.highlevelil.HighLevelILDoWhileSsa`](#binaryninja.highlevelil.HighLevelILDoWhileSsa "binaryninja.highlevelil.HighLevelILDoWhileSsa") |  |
| [`binaryninja.highlevelil.HighLevelILExternPtr`](#binaryninja.highlevelil.HighLevelILExternPtr "binaryninja.highlevelil.HighLevelILExternPtr") |  |
| [`binaryninja.highlevelil.HighLevelILFabs`](#binaryninja.highlevelil.HighLevelILFabs "binaryninja.highlevelil.HighLevelILFabs") |  |
| [`binaryninja.highlevelil.HighLevelILFadd`](#binaryninja.highlevelil.HighLevelILFadd "binaryninja.highlevelil.HighLevelILFadd") |  |
| [`binaryninja.highlevelil.HighLevelILFcmpE`](#binaryninja.highlevelil.HighLevelILFcmpE "binaryninja.highlevelil.HighLevelILFcmpE") |  |
| [`binaryninja.highlevelil.HighLevelILFcmpGe`](#binaryninja.highlevelil.HighLevelILFcmpGe "binaryninja.highlevelil.HighLevelILFcmpGe") |  |
| [`binaryninja.highlevelil.HighLevelILFcmpGt`](#binaryninja.highlevelil.HighLevelILFcmpGt "binaryninja.highlevelil.HighLevelILFcmpGt") |  |
| [`binaryninja.highlevelil.HighLevelILFcmpLe`](#binaryninja.highlevelil.HighLevelILFcmpLe "binaryninja.highlevelil.HighLevelILFcmpLe") |  |
| [`binaryninja.highlevelil.HighLevelILFcmpLt`](#binaryninja.highlevelil.HighLevelILFcmpLt "binaryninja.highlevelil.HighLevelILFcmpLt") |  |
| [`binaryninja.highlevelil.HighLevelILFcmpNe`](#binaryninja.highlevelil.HighLevelILFcmpNe "binaryninja.highlevelil.HighLevelILFcmpNe") |  |
| [`binaryninja.highlevelil.HighLevelILFcmpO`](#binaryninja.highlevelil.HighLevelILFcmpO "binaryninja.highlevelil.HighLevelILFcmpO") |  |
| [`binaryninja.highlevelil.HighLevelILFcmpUo`](#binaryninja.highlevelil.HighLevelILFcmpUo "binaryninja.highlevelil.HighLevelILFcmpUo") |  |
| [`binaryninja.highlevelil.HighLevelILFdiv`](#binaryninja.highlevelil.HighLevelILFdiv "binaryninja.highlevelil.HighLevelILFdiv") |  |
| [`binaryninja.highlevelil.HighLevelILFloatConst`](#binaryninja.highlevelil.HighLevelILFloatConst "binaryninja.highlevelil.HighLevelILFloatConst") |  |
| [`binaryninja.highlevelil.HighLevelILFloatConv`](#binaryninja.highlevelil.HighLevelILFloatConv "binaryninja.highlevelil.HighLevelILFloatConv") |  |
| [`binaryninja.highlevelil.HighLevelILFloatToInt`](#binaryninja.highlevelil.HighLevelILFloatToInt "binaryninja.highlevelil.HighLevelILFloatToInt") |  |
| [`binaryninja.highlevelil.HighLevelILFloor`](#binaryninja.highlevelil.HighLevelILFloor "binaryninja.highlevelil.HighLevelILFloor") |  |
| [`binaryninja.highlevelil.HighLevelILFmul`](#binaryninja.highlevelil.HighLevelILFmul "binaryninja.highlevelil.HighLevelILFmul") |  |
| [`binaryninja.highlevelil.HighLevelILFneg`](#binaryninja.highlevelil.HighLevelILFneg "binaryninja.highlevelil.HighLevelILFneg") |  |
| [`binaryninja.highlevelil.HighLevelILFor`](#binaryninja.highlevelil.HighLevelILFor "binaryninja.highlevelil.HighLevelILFor") |  |
| [`binaryninja.highlevelil.HighLevelILForSsa`](#binaryninja.highlevelil.HighLevelILForSsa "binaryninja.highlevelil.HighLevelILForSsa") |  |
| [`binaryninja.highlevelil.HighLevelILForceVer`](#binaryninja.highlevelil.HighLevelILForceVer "binaryninja.highlevelil.HighLevelILForceVer") |  |
| [`binaryninja.highlevelil.HighLevelILForceVerSsa`](#binaryninja.highlevelil.HighLevelILForceVerSsa "binaryninja.highlevelil.HighLevelILForceVerSsa") |  |
| [`binaryninja.highlevelil.HighLevelILFsqrt`](#binaryninja.highlevelil.HighLevelILFsqrt "binaryninja.highlevelil.HighLevelILFsqrt") |  |
| [`binaryninja.highlevelil.HighLevelILFsub`](#binaryninja.highlevelil.HighLevelILFsub "binaryninja.highlevelil.HighLevelILFsub") |  |
| [`binaryninja.highlevelil.HighLevelILFtrunc`](#binaryninja.highlevelil.HighLevelILFtrunc "binaryninja.highlevelil.HighLevelILFtrunc") |  |
| [`binaryninja.highlevelil.HighLevelILFunction`](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | `class HighLevelILFunction` contains the a HighLevelILInstruction object that makes up the… |
| [`binaryninja.highlevelil.HighLevelILGoto`](#binaryninja.highlevelil.HighLevelILGoto "binaryninja.highlevelil.HighLevelILGoto") |  |
| [`binaryninja.highlevelil.HighLevelILIf`](#binaryninja.highlevelil.HighLevelILIf "binaryninja.highlevelil.HighLevelILIf") |  |
| [`binaryninja.highlevelil.HighLevelILImport`](#binaryninja.highlevelil.HighLevelILImport "binaryninja.highlevelil.HighLevelILImport") |  |
| [`binaryninja.highlevelil.HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | `class HighLevelILInstruction` High Level Intermediate Language Instructions form an abstract… |
| [`binaryninja.highlevelil.HighLevelILIntToFloat`](#binaryninja.highlevelil.HighLevelILIntToFloat "binaryninja.highlevelil.HighLevelILIntToFloat") |  |
| [`binaryninja.highlevelil.HighLevelILIntrinsic`](#binaryninja.highlevelil.HighLevelILIntrinsic "binaryninja.highlevelil.HighLevelILIntrinsic") |  |
| [`binaryninja.highlevelil.HighLevelILIntrinsicSsa`](#binaryninja.highlevelil.HighLevelILIntrinsicSsa "binaryninja.highlevelil.HighLevelILIntrinsicSsa") |  |
| [`binaryninja.highlevelil.HighLevelILJump`](#binaryninja.highlevelil.HighLevelILJump "binaryninja.highlevelil.HighLevelILJump") |  |
| [`binaryninja.highlevelil.HighLevelILLabel`](#binaryninja.highlevelil.HighLevelILLabel "binaryninja.highlevelil.HighLevelILLabel") |  |
| [`binaryninja.highlevelil.HighLevelILLowPart`](#binaryninja.highlevelil.HighLevelILLowPart "binaryninja.highlevelil.HighLevelILLowPart") |  |
| [`binaryninja.highlevelil.HighLevelILLsl`](#binaryninja.highlevelil.HighLevelILLsl "binaryninja.highlevelil.HighLevelILLsl") |  |
| [`binaryninja.highlevelil.HighLevelILLsr`](#binaryninja.highlevelil.HighLevelILLsr "binaryninja.highlevelil.HighLevelILLsr") |  |
| [`binaryninja.highlevelil.HighLevelILMemPhi`](#binaryninja.highlevelil.HighLevelILMemPhi "binaryninja.highlevelil.HighLevelILMemPhi") |  |
| [`binaryninja.highlevelil.HighLevelILMods`](#binaryninja.highlevelil.HighLevelILMods "binaryninja.highlevelil.HighLevelILMods") |  |
| [`binaryninja.highlevelil.HighLevelILModsDp`](#binaryninja.highlevelil.HighLevelILModsDp "binaryninja.highlevelil.HighLevelILModsDp") |  |
| [`binaryninja.highlevelil.HighLevelILModu`](#binaryninja.highlevelil.HighLevelILModu "binaryninja.highlevelil.HighLevelILModu") |  |
| [`binaryninja.highlevelil.HighLevelILModuDp`](#binaryninja.highlevelil.HighLevelILModuDp "binaryninja.highlevelil.HighLevelILModuDp") |  |
| [`binaryninja.highlevelil.HighLevelILMul`](#binaryninja.highlevelil.HighLevelILMul "binaryninja.highlevelil.HighLevelILMul") |  |
| [`binaryninja.highlevelil.HighLevelILMulsDp`](#binaryninja.highlevelil.HighLevelILMulsDp "binaryninja.highlevelil.HighLevelILMulsDp") |  |
| [`binaryninja.highlevelil.HighLevelILMuluDp`](#binaryninja.highlevelil.HighLevelILMuluDp "binaryninja.highlevelil.HighLevelILMuluDp") |  |
| [`binaryninja.highlevelil.HighLevelILNeg`](#binaryninja.highlevelil.HighLevelILNeg "binaryninja.highlevelil.HighLevelILNeg") |  |
| [`binaryninja.highlevelil.HighLevelILNop`](#binaryninja.highlevelil.HighLevelILNop "binaryninja.highlevelil.HighLevelILNop") |  |
| [`binaryninja.highlevelil.HighLevelILNoret`](#binaryninja.highlevelil.HighLevelILNoret "binaryninja.highlevelil.HighLevelILNoret") |  |
| [`binaryninja.highlevelil.HighLevelILNot`](#binaryninja.highlevelil.HighLevelILNot "binaryninja.highlevelil.HighLevelILNot") |  |
| [`binaryninja.highlevelil.HighLevelILOperationAndSize`](#binaryninja.highlevelil.HighLevelILOperationAndSize "binaryninja.highlevelil.HighLevelILOperationAndSize") |  |
| [`binaryninja.highlevelil.HighLevelILOr`](#binaryninja.highlevelil.HighLevelILOr "binaryninja.highlevelil.HighLevelILOr") |  |
| [`binaryninja.highlevelil.HighLevelILRet`](#binaryninja.highlevelil.HighLevelILRet "binaryninja.highlevelil.HighLevelILRet") |  |
| [`binaryninja.highlevelil.HighLevelILRlc`](#binaryninja.highlevelil.HighLevelILRlc "binaryninja.highlevelil.HighLevelILRlc") |  |
| [`binaryninja.highlevelil.HighLevelILRol`](#binaryninja.highlevelil.HighLevelILRol "binaryninja.highlevelil.HighLevelILRol") |  |
| [`binaryninja.highlevelil.HighLevelILRor`](#binaryninja.highlevelil.HighLevelILRor "binaryninja.highlevelil.HighLevelILRor") |  |
| [`binaryninja.highlevelil.HighLevelILRoundToInt`](#binaryninja.highlevelil.HighLevelILRoundToInt "binaryninja.highlevelil.HighLevelILRoundToInt") |  |
| [`binaryninja.highlevelil.HighLevelILRrc`](#binaryninja.highlevelil.HighLevelILRrc "binaryninja.highlevelil.HighLevelILRrc") |  |
| [`binaryninja.highlevelil.HighLevelILSbb`](#binaryninja.highlevelil.HighLevelILSbb "binaryninja.highlevelil.HighLevelILSbb") |  |
| [`binaryninja.highlevelil.HighLevelILSplit`](#binaryninja.highlevelil.HighLevelILSplit "binaryninja.highlevelil.HighLevelILSplit") |  |
| [`binaryninja.highlevelil.HighLevelILStructField`](#binaryninja.highlevelil.HighLevelILStructField "binaryninja.highlevelil.HighLevelILStructField") |  |
| [`binaryninja.highlevelil.HighLevelILSub`](#binaryninja.highlevelil.HighLevelILSub "binaryninja.highlevelil.HighLevelILSub") |  |
| [`binaryninja.highlevelil.HighLevelILSwitch`](#binaryninja.highlevelil.HighLevelILSwitch "binaryninja.highlevelil.HighLevelILSwitch") |  |
| [`binaryninja.highlevelil.HighLevelILSx`](#binaryninja.highlevelil.HighLevelILSx "binaryninja.highlevelil.HighLevelILSx") |  |
| [`binaryninja.highlevelil.HighLevelILSyscall`](#binaryninja.highlevelil.HighLevelILSyscall "binaryninja.highlevelil.HighLevelILSyscall") |  |
| [`binaryninja.highlevelil.HighLevelILSyscallSsa`](#binaryninja.highlevelil.HighLevelILSyscallSsa "binaryninja.highlevelil.HighLevelILSyscallSsa") |  |
| [`binaryninja.highlevelil.HighLevelILTailcall`](#binaryninja.highlevelil.HighLevelILTailcall "binaryninja.highlevelil.HighLevelILTailcall") |  |
| [`binaryninja.highlevelil.HighLevelILTestBit`](#binaryninja.highlevelil.HighLevelILTestBit "binaryninja.highlevelil.HighLevelILTestBit") |  |
| [`binaryninja.highlevelil.HighLevelILTrap`](#binaryninja.highlevelil.HighLevelILTrap "binaryninja.highlevelil.HighLevelILTrap") |  |
| [`binaryninja.highlevelil.HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase "binaryninja.highlevelil.HighLevelILUnaryBase") |  |
| [`binaryninja.highlevelil.HighLevelILUndef`](#binaryninja.highlevelil.HighLevelILUndef "binaryninja.highlevelil.HighLevelILUndef") |  |
| [`binaryninja.highlevelil.HighLevelILUnimpl`](#binaryninja.highlevelil.HighLevelILUnimpl "binaryninja.highlevelil.HighLevelILUnimpl") |  |
| [`binaryninja.highlevelil.HighLevelILUnimplMem`](#binaryninja.highlevelil.HighLevelILUnimplMem "binaryninja.highlevelil.HighLevelILUnimplMem") |  |
| [`binaryninja.highlevelil.HighLevelILUnreachable`](#binaryninja.highlevelil.HighLevelILUnreachable "binaryninja.highlevelil.HighLevelILUnreachable") |  |
| [`binaryninja.highlevelil.HighLevelILVar`](#binaryninja.highlevelil.HighLevelILVar "binaryninja.highlevelil.HighLevelILVar") |  |
| [`binaryninja.highlevelil.HighLevelILVarDeclare`](#binaryninja.highlevelil.HighLevelILVarDeclare "binaryninja.highlevelil.HighLevelILVarDeclare") |  |
| [`binaryninja.highlevelil.HighLevelILVarInit`](#binaryninja.highlevelil.HighLevelILVarInit "binaryninja.highlevelil.HighLevelILVarInit") |  |
| [`binaryninja.highlevelil.HighLevelILVarInitSsa`](#binaryninja.highlevelil.HighLevelILVarInitSsa "binaryninja.highlevelil.HighLevelILVarInitSsa") |  |
| [`binaryninja.highlevelil.HighLevelILVarPhi`](#binaryninja.highlevelil.HighLevelILVarPhi "binaryninja.highlevelil.HighLevelILVarPhi") |  |
| [`binaryninja.highlevelil.HighLevelILVarSsa`](#binaryninja.highlevelil.HighLevelILVarSsa "binaryninja.highlevelil.HighLevelILVarSsa") |  |
| [`binaryninja.highlevelil.HighLevelILWhile`](#binaryninja.highlevelil.HighLevelILWhile "binaryninja.highlevelil.HighLevelILWhile") |  |
| [`binaryninja.highlevelil.HighLevelILWhileSsa`](#binaryninja.highlevelil.HighLevelILWhileSsa "binaryninja.highlevelil.HighLevelILWhileSsa") |  |
| [`binaryninja.highlevelil.HighLevelILXor`](#binaryninja.highlevelil.HighLevelILXor "binaryninja.highlevelil.HighLevelILXor") |  |
| [`binaryninja.highlevelil.HighLevelILZx`](#binaryninja.highlevelil.HighLevelILZx "binaryninja.highlevelil.HighLevelILZx") |  |

## CoreHighLevelILInstruction

*class* CoreHighLevelILInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#CoreHighLevelILInstruction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    CoreHighLevelILInstruction(operation: binaryninja.enums.HighLevelILOperation,
    attributes: int, source_operand: int, size: int, operands: Tuple[ExpressionIndex,
    ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex], address: int,
    parent: <function NewType.<locals>.new_type at 0x105107820>)

    __init__(*operation: [HighLevelILOperation](enums.md#binaryninja.enums.HighLevelILOperation "binaryninja.enums.HighLevelILOperation")*, *attributes: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *source_operand: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *operands: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*, *address: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *parent: ExpressionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **operation** ([*HighLevelILOperation*](enums.md#binaryninja.enums.HighLevelILOperation
              "binaryninja.enums.HighLevelILOperation")) –
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
            - **parent** (*ExpressionIndex*) –

        Return type:
        :   *None*

    *classmethod* from_BNHighLevelILInstruction(*instr: BNHighLevelILInstruction*) → [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#CoreHighLevelILInstruction.from_BNHighLevelILInstruction)
    :   Parameters:
        :   **instr** (*BNHighLevelILInstruction*) –

        Return type:
        :   [*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
            "binaryninja.highlevelil.CoreHighLevelILInstruction")

    address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    attributes*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    operands*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*

    operation*: [HighLevelILOperation](enums.md#binaryninja.enums.HighLevelILOperation "binaryninja.enums.HighLevelILOperation")*

    parent*: ExpressionIndex*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    source_operand*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## GotoLabel

*class* GotoLabel[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#GotoLabel)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    GotoLabel(function: ‘HighLevelILFunction’, id: int)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **id** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    *property* definition*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* label_id*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*

    *property* uses*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

## HighLevelILAdc

*class* HighLevelILAdc[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAdc)
:   Bases: [`HighLevelILCarryBase`](#binaryninja.highlevelil.HighLevelILCarryBase
    "binaryninja.highlevelil.HighLevelILCarryBase")

    HighLevelILAdc(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILAdd

*class* HighLevelILAdd[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAdd)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILAdd(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILAddOverflow

*class* HighLevelILAddOverflow[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAddOverflow)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILAddOverflow(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILAddressOf

*class* HighLevelILAddressOf[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAddressOf)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase")

    HighLevelILAddressOf(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* vars_address_taken*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   Non-unique list of variables whose address is taken by instruction

        Note

        This property has some nuance to it, so use carefully. This property will return only
        those variable which directly have their address taken such as &var_4 or &var_8.d but
        not those which are involved in an address calculation such as &(var_4 + 0) or &var_4[0]
        even though they may be functionally equivalent.

## HighLevelILAnd

*class* HighLevelILAnd[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAnd)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILAnd(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILArrayIndex

*class* HighLevelILArrayIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILArrayIndex)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILArrayIndex(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    *property* index*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILArrayIndexSsa

*class* HighLevelILArrayIndexSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILArrayIndexSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILArrayIndexSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    *property* index*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILAsr

*class* HighLevelILAsr[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAsr)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILAsr(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILAssert

*class* HighLevelILAssert[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAssert)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILAssert(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* constraint*: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## HighLevelILAssertSsa

*class* HighLevelILAssertSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAssertSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILAssertSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* constraint*: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## HighLevelILAssign

*class* HighLevelILAssign[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAssign)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar")

    HighLevelILAssign(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables value is written by this instruction

## HighLevelILAssignMemSsa

*class* HighLevelILAssignMemSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAssignMemSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILAssignMemSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILAssignUnpack

*class* HighLevelILAssignUnpack[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAssignUnpack)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar")

    HighLevelILAssignUnpack(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables value is written by this instruction

## HighLevelILAssignUnpackMemSsa

*class* HighLevelILAssignUnpackMemSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILAssignUnpackMemSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA"),
    [`Memory`](commonil.md#binaryninja.commonil.Memory "binaryninja.commonil.Memory")

    HighLevelILAssignUnpackMemSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILBasicBlock

*class* HighLevelILBasicBlock[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILBasicBlock)
:   Bases: [`BasicBlock`](basicblock.md#binaryninja.basicblock.BasicBlock
    "binaryninja.basicblock.BasicBlock")

    The `HighLevelILBasicBlock` object is returned during analysis and should not be
    directly instantiated.

    __init__(*handle: LP_BNBasicBlock*, *owner: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *view: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*)[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILBasicBlock.__init__)
    :   Parameters:
        :   - **handle** (*LP_BNBasicBlock*) –
            - **owner** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **view** ([*BinaryView*](binaryview.md#binaryninja.binaryview.BinaryView
              "binaryninja.binaryview.BinaryView") *|* *None*) –

    *property* il_function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*
    :   IL Function of which this block is a part, if the block is part of an IL Function.

    *property* instruction_count*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILBinaryBase

*class* HighLevelILBinaryBase[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILBinaryBase)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`BinaryOperation`](commonil.md#binaryninja.commonil.BinaryOperation
    "binaryninja.commonil.BinaryOperation")

    HighLevelILBinaryBase(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* left*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* right*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILBlock

*class* HighLevelILBlock[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILBlock)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILBlock(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* body*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILBoolToInt

*class* HighLevelILBoolToInt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILBoolToInt)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase")

    HighLevelILBoolToInt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILBp

*class* HighLevelILBp[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILBp)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    HighLevelILBp(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILBreak

*class* HighLevelILBreak[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILBreak)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    HighLevelILBreak(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCall

*class* HighLevelILCall[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCall)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Localcall`](commonil.md#binaryninja.commonil.Localcall
    "binaryninja.commonil.Localcall")

    HighLevelILCall(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

## HighLevelILCallSsa

*class* HighLevelILCallSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCallSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Localcall`](commonil.md#binaryninja.commonil.Localcall
    "binaryninja.commonil.Localcall"), [`SSA`](commonil.md#binaryninja.commonil.SSA
    "binaryninja.commonil.SSA")

    HighLevelILCallSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILCarryBase

*class* HighLevelILCarryBase[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCarryBase)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILCarryBase(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* carry*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* left*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* right*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILCase

*class* HighLevelILCase[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCase)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILCase(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* body*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* values*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

## HighLevelILCeil

*class* HighLevelILCeil[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCeil)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILCeil(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpE

*class* HighLevelILCmpE[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpE)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase")

    HighLevelILCmpE(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpNe

*class* HighLevelILCmpNe[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpNe)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase")

    HighLevelILCmpNe(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpSge

*class* HighLevelILCmpSge[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpSge)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    HighLevelILCmpSge(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpSgt

*class* HighLevelILCmpSgt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpSgt)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    HighLevelILCmpSgt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpSle

*class* HighLevelILCmpSle[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpSle)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    HighLevelILCmpSle(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpSlt

*class* HighLevelILCmpSlt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpSlt)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    HighLevelILCmpSlt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpUge

*class* HighLevelILCmpUge[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpUge)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase")

    HighLevelILCmpUge(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpUgt

*class* HighLevelILCmpUgt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpUgt)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase")

    HighLevelILCmpUgt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpUle

*class* HighLevelILCmpUle[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpUle)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase")

    HighLevelILCmpUle(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILCmpUlt

*class* HighLevelILCmpUlt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILCmpUlt)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase")

    HighLevelILCmpUlt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILComparisonBase

*class* HighLevelILComparisonBase[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILComparisonBase)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Comparison`](commonil.md#binaryninja.commonil.Comparison
    "binaryninja.commonil.Comparison")

    HighLevelILComparisonBase(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILConst

*class* HighLevelILConst[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILConst)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Constant`](commonil.md#binaryninja.commonil.Constant "binaryninja.commonil.Constant")

    HighLevelILConst(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILConstData

*class* HighLevelILConstData[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILConstData)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Constant`](commonil.md#binaryninja.commonil.Constant "binaryninja.commonil.Constant")

    HighLevelILConstData(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* constant*: [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData")*

    *property* constant_data*: [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILConstPtr

*class* HighLevelILConstPtr[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILConstPtr)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Constant`](commonil.md#binaryninja.commonil.Constant "binaryninja.commonil.Constant")

    HighLevelILConstPtr(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* string*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [StringType](enums.md#binaryninja.enums.StringType "binaryninja.enums.StringType")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

## HighLevelILContinue

*class* HighLevelILContinue[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILContinue)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`ControlFlow`](commonil.md#binaryninja.commonil.ControlFlow
    "binaryninja.commonil.ControlFlow")

    HighLevelILContinue(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILDeref

*class* HighLevelILDeref[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDeref)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase")

    HighLevelILDeref(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILDerefField

*class* HighLevelILDerefField[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDerefField)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILDerefField(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* member_index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILDerefFieldSsa

*class* HighLevelILDerefFieldSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDerefFieldSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILDerefFieldSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* member_index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILDerefSsa

*class* HighLevelILDerefSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDerefSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILDerefSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILDivs

*class* HighLevelILDivs[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDivs)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    HighLevelILDivs(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILDivsDp

*class* HighLevelILDivsDp[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDivsDp)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    HighLevelILDivsDp(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILDivu

*class* HighLevelILDivu[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDivu)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILDivu(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILDivuDp

*class* HighLevelILDivuDp[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDivuDp)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    HighLevelILDivuDp(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILDoWhile

*class* HighLevelILDoWhile[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDoWhile)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Loop`](commonil.md#binaryninja.commonil.Loop "binaryninja.commonil.Loop")

    HighLevelILDoWhile(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* body*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* condition*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILDoWhileSsa

*class* HighLevelILDoWhileSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILDoWhileSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Loop`](commonil.md#binaryninja.commonil.Loop "binaryninja.commonil.Loop"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILDoWhileSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* body*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* condition*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* condition_phi*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILExternPtr

*class* HighLevelILExternPtr[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILExternPtr)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Constant`](commonil.md#binaryninja.commonil.Constant "binaryninja.commonil.Constant")

    HighLevelILExternPtr(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILFabs

*class* HighLevelILFabs[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFabs)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFabs(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFadd

*class* HighLevelILFadd[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFadd)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFadd(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFcmpE

*class* HighLevelILFcmpE[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFcmpE)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFcmpE(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFcmpGe

*class* HighLevelILFcmpGe[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFcmpGe)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFcmpGe(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFcmpGt

*class* HighLevelILFcmpGt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFcmpGt)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFcmpGt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFcmpLe

*class* HighLevelILFcmpLe[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFcmpLe)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFcmpLe(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFcmpLt

*class* HighLevelILFcmpLt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFcmpLt)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFcmpLt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFcmpNe

*class* HighLevelILFcmpNe[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFcmpNe)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFcmpNe(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFcmpO

*class* HighLevelILFcmpO[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFcmpO)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFcmpO(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFcmpUo

*class* HighLevelILFcmpUo[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFcmpUo)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFcmpUo(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFdiv

*class* HighLevelILFdiv[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFdiv)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFdiv(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFloatConst

*class* HighLevelILFloatConst[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFloatConst)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Constant`](commonil.md#binaryninja.commonil.Constant "binaryninja.commonil.Constant")

    HighLevelILFloatConst(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* constant*: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFloatConv

*class* HighLevelILFloatConv[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFloatConv)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFloatConv(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFloatToInt

*class* HighLevelILFloatToInt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFloatToInt)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFloatToInt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFloor

*class* HighLevelILFloor[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFloor)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFloor(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFmul

*class* HighLevelILFmul[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFmul)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFmul(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFneg

*class* HighLevelILFneg[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFneg)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFneg(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFor

*class* HighLevelILFor[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFor)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Loop`](commonil.md#binaryninja.commonil.Loop "binaryninja.commonil.Loop")

    HighLevelILFor(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* body*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* condition*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    *property* init*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* update*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILForSsa

*class* HighLevelILForSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILForSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Loop`](commonil.md#binaryninja.commonil.Loop "binaryninja.commonil.Loop"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILForSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* body*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* condition*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* condition_phi*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    *property* init*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* update*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILForceVer

*class* HighLevelILForceVer[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILForceVer)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILForceVer(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## HighLevelILForceVerSsa

*class* HighLevelILForceVerSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILForceVerSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILForceVerSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## HighLevelILFsqrt

*class* HighLevelILFsqrt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFsqrt)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFsqrt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFsub

*class* HighLevelILFsub[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFsub)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFsub(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFtrunc

*class* HighLevelILFtrunc[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFtrunc)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILFtrunc(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILFunction

*class* HighLevelILFunction[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    `class HighLevelILFunction` contains the a HighLevelILInstruction object that makes up
    the abstract syntax tree of a function.

    __init__(*arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *handle: BNHighLevelILFunction | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *source_func: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.__init__)
    :   Parameters:
        :   - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –
            - **handle** (*BNHighLevelILFunction* *|* *None*) –
            - **source_func** ([*Function*](function.md#binaryninja.function.Function
              "binaryninja.function.Function") *|* *None*) –

    add(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.add)
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

    add_carry(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.add_carry)
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

    add_operand_list(*operands: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.add_operand_list)
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

    address_of(*src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.address_of)
    :   `address_of` takes the address of `src`

        Parameters:
        :   - **src** (*ExpressionIndex*) – the expression having its address taken
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `&src`

        Return type:
        :   ExpressionIndex

    and_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.and_expr)
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

    arith_shift_right(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.arith_shift_right)
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

    array_index(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: ExpressionIndex*, *idx: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.array_index)
    :   `array_index` references an item at index `idx` in the array in `src` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the item in the array
            - **src** (*ExpressionIndex*) – expression for the array
            - **idx** (*ExpressionIndex*) – expression for the index into the array
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `src[idx].size`

        Return type:
        :   ExpressionIndex

    assign(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *dest: ExpressionIndex*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.assign)
    :   `assign` assign expression `src` to expression `dest`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the expression
            - **dest** (*ExpressionIndex*) – expression being assigned
            - **src** (*ExpressionIndex*) – value being assigned to the expression
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `dest = src`

        Return type:
        :   ExpressionIndex

    assign_unpack(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *output: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.assign_unpack)
    :   `assign_unpack` assign expression `src` to a list of expressions in `output` of size
        `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the expression
            - **output** (*List**[**ExpressionIndex**]*) – expressions being assigned
            - **src** (*ExpressionIndex*) – value being assigned to the expressions
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `output... = src`

        Return type:
        :   ExpressionIndex

    block(*exprs: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.block)
    :   `block` a block expression containing multiple child expressions

        Parameters:
        :   - **exprs** (*List**[**ExpressionIndex**]*) – child expressions in the block
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `` { exprs… } ``

        Return type:
        :   ExpressionIndex

    bool_to_int(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.bool_to_int)
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

    break_expr(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.break_expr)
    :   `break` break out of a loop or switch statement

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `break`

        Return type:
        :   ExpressionIndex

    breakpoint(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.breakpoint)
    :   `breakpoint` returns a processor breakpoint expression.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   a breakpoint expression.

        Return type:
        :   ExpressionIndex

    call(*dest: ExpressionIndex*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.call)
    :   `call` returns an expression which calls the function in the expression `dest` with the
        parameters defined in `params`

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression to call
            - **params** (*List**[**ExpressionIndex**]*) – parameter variables
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `call(dest, params...)`

        Return type:
        :   ExpressionIndex

    case(*values: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *expr: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.case)
    :   `case` a switch case for values `values` with body `expr`

        Parameters:
        :   - **values** (*List**[**ExpressionIndex**]*) – matched values for the case
            - **expr** (*ExpressionIndex*) – body of switch case
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `case values...: { expr }`

        Return type:
        :   ExpressionIndex

    ceil(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.ceil)
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

    compare_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_equal)
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

    compare_not_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_not_equal)
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

    compare_signed_greater_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_signed_greater_equal)
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

    compare_signed_greater_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_signed_greater_than)
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

    compare_signed_less_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_signed_less_equal)
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

    compare_signed_less_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_signed_less_than)
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

    compare_unsigned_greater_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_unsigned_greater_equal)
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

    compare_unsigned_greater_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_unsigned_greater_than)
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

    compare_unsigned_less_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_unsigned_less_equal)
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

    compare_unsigned_less_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.compare_unsigned_less_than)
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

    const(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.const)
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

    const_data(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *data: [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.const_data)
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

    const_pointer(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.const_pointer)
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

    continue_expr(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.continue_expr)
    :   `continue` continue to the top of a loop statement

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `continue`

        Return type:
        :   ExpressionIndex

    copy_expr(*original: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.copy_expr)
    :   `copy_expr` adds an expression to the function which is equivalent to the given
        expression

        Parameters:
        :   **original** ([*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction")) – the original IL Instruction you
            want to copy

        Returns:
        :   The index of the newly copied expression

        Return type:
        :   ExpressionIndex

    create_graph(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreFlowGraph](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.create_graph)
    :   Parameters:
        :   **settings**
            ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*CoreFlowGraph*](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph
            "binaryninja.flowgraph.CoreFlowGraph")

    create_graph_immediate(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [CoreFlowGraph](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph "binaryninja.flowgraph.CoreFlowGraph")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.create_graph_immediate)
    :   Parameters:
        :   **settings**
            ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*CoreFlowGraph*](flowgraph.md#binaryninja.flowgraph.CoreFlowGraph
            "binaryninja.flowgraph.CoreFlowGraph")

    deref(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.deref)
    :   `deref` dereferences expression `src` and reads a value of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the read
            - **src** (*ExpressionIndex*) – expression being read
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `(*src).size`

        Return type:
        :   ExpressionIndex

    deref_field(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: ExpressionIndex*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *member_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.deref_field)
    :   `deref_field` dereferences structure field in expression `src` at offset `offset` and
        index `member_index` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the read
            - **src** (*ExpressionIndex*) – expression of structure being read
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of field in the structure
            - **member_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – index of field in the structure
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `src->offset.size`

        Return type:
        :   ExpressionIndex

    div_double_prec_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.div_double_prec_signed)
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

    div_double_prec_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.div_double_prec_unsigned)
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

    div_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.div_signed)
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

    div_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.div_unsigned)
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

    do_while_expr(*condition: ExpressionIndex*, *loop_expr: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.do_while_expr)
    :   `do_while_expr` a do-while-loop expression with a condition and loop body.

        Parameters:
        :   - **condition** (*ExpressionIndex*) – expression for the loop condition
            - **loop_expr** (*ExpressionIndex*) – expression for the loop body
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `do { loop_expr } while (condition)`

        Return type:
        :   ExpressionIndex

    expr(*operation: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [HighLevelILOperation](enums.md#binaryninja.enums.HighLevelILOperation "binaryninja.enums.HighLevelILOperation")*, *a: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *b: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *c: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *d: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *e: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *source_location: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.expr)
    :   Parameters:
        :   - **operation** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)") *|* [*HighLevelILOperation*](enums.md#binaryninja.enums.HighLevelILOperation
              "binaryninja.enums.HighLevelILOperation")) –
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

    extern_pointer(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.extern_pointer)
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

    finalize() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.finalize)
    :   `finalize` ends the function and computes the list of basic blocks.

        Return type:
        :   *None*

    float_abs(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_abs)
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

    float_add(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_add)
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

    float_compare_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_compare_equal)
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

    float_compare_greater_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_compare_greater_equal)
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

    float_compare_greater_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_compare_greater_than)
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

    float_compare_less_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_compare_less_equal)
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

    float_compare_less_than(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_compare_less_than)
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

    float_compare_not_equal(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_compare_not_equal)
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

    float_compare_ordered(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_compare_ordered)
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

    float_compare_unordered(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_compare_unordered)
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

    float_const_double(*value: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_const_double)
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

    float_const_raw(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_const_raw)
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

    float_const_single(*value: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_const_single)
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

    float_convert(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_convert)
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

    float_div(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_div)
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

    float_mult(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_mult)
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

    float_neg(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_neg)
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

    float_sqrt(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_sqrt)
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

    float_sub(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_sub)
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

    float_to_int(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_to_int)
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

    float_trunc(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.float_trunc)
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

    floor(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.floor)
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

    for_expr(*init_expr: ExpressionIndex*, *condition: ExpressionIndex*, *update_expr: ExpressionIndex*, *loop_expr: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.for_expr)
    :   `for-expr` a for-loop expression with an initializer, condition, updater, and loop body.

        Parameters:
        :   - **init_expr** (*ExpressionIndex*) – expression for the loop initializer
            - **condition** (*ExpressionIndex*) – expression for the loop condition
            - **update_expr** (*ExpressionIndex*) – expression for the loop updater
            - **loop_expr** (*ExpressionIndex*) – expression for the loop body
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `for (init_expr ; condition ; update_expr) { loop_expr }`

        Return type:
        :   ExpressionIndex

    generate_ssa_form(*variables: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.generate_ssa_form)
    :   `generate_ssa_form` generate SSA form given the current HLIL

        Parameters:
        :   **variables** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python
            v3.14)")*(*[*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")*)*) – optional list of aliased variables

        Return type:
        :   *None*

    get_basic_block_at(*index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [HighLevelILBasicBlock](#binaryninja.highlevelil.HighLevelILBasicBlock "binaryninja.highlevelil.HighLevelILBasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_basic_block_at)
    :   `get_basic_block_at` returns the BasicBlock at the given HLIL instruction `index`.

        Parameters:
        :   **index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – Index of the HLIL instruction of the BasicBlock to retrieve.

        Example:
        :   ```
            >>> current_il_function.get_basic_block_at(current_il_index)
            <llil block: x86@19-26>
            ```

        Return type:
        :   [*HighLevelILBasicBlock*](#binaryninja.highlevelil.HighLevelILBasicBlock
            "binaryninja.highlevelil.HighLevelILBasicBlock") | *None*

    get_expr(*index: ExpressionIndex*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_expr)
    :   `get_expr` retrieves the IL expression at a given expression index in the function.

        Warning

        Not all IL expressions are valid, even if their index is within the bounds of the
        function, they might not be used by the function and might not contain properly
        structured data.

        Parameters:
        :   - **index** (*ExpressionIndex*) – Index of desired expression in function
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether to return the expression as a full AST or a single instruction
              (defaults to AST)

        Returns:
        :   A HighLevelILInstruction object for the expression, if it exists. Otherwise, None

        Return type:
        :   [*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction") | *None*

    get_expr_count() → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_expr_count)
    :   `get_expr_count` gives a the total number of expressions in this IL function

        You can use this to enumerate all expressions in conjunction with
        [`get_expr`](#binaryninja.highlevelil.HighLevelILFunction.get_expr
        "binaryninja.highlevelil.HighLevelILFunction.get_expr")

        Warning

        Not all IL expressions are valid, even if their index is within the bounds of the
        function, they might not be used by the function and might not contain properly
        structured data.

        Returns:
        :   The number of expressions in the function

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_expr_index_for_instruction(*instr: InstructionIndex*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_expr_index_for_instruction)
    :   Parameters:
        :   **instr** (*InstructionIndex*) –

        Return type:
        :   ExpressionIndex

    get_expr_type(*expr_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_expr_type)
    :   Get type of expression

        Parameters:
        :   **expr_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) – index of the expression to retrieve

        Return type:
        :   *Optional*[’types.Type’]

    get_instruction_index_for_expr(*expr: ExpressionIndex*) → InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_instruction_index_for_expr)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   InstructionIndex | *None*

    get_label(*label_idx: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_label)
    :   Parameters:
        :   **label_idx** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction") | *None*

    get_label_uses(*label_idx: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_label_uses)
    :   Parameters:
        :   **label_idx** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction")]

    get_medium_level_il_expr_index(*expr: ExpressionIndex*) → ExpressionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_medium_level_il_expr_index)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   ExpressionIndex | *None*

    get_medium_level_il_expr_indexes(*expr: ExpressionIndex*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex][[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_medium_level_il_expr_indexes)
    :   Parameters:
        :   **expr** (*ExpressionIndex*) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[ExpressionIndex]

    get_non_ssa_instruction_index(*instr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_non_ssa_instruction_index)
    :   Parameters:
        :   **instr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_ssa_instruction_index(*instr: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_ssa_instruction_index)
    :   Parameters:
        :   **instr** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_ssa_memory_definition(*version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_ssa_memory_definition)
    :   Parameters:
        :   **version** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction") | *None*

    get_ssa_memory_uses(*version: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_ssa_memory_uses)
    :   Parameters:
        :   **version** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
            v3.14)")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction")]

    get_ssa_var_definition(*ssa_var: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [HighLevelILVarSsa](#binaryninja.highlevelil.HighLevelILVarSsa "binaryninja.highlevelil.HighLevelILVarSsa")*) → [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_ssa_var_definition)
    :   Gets the instruction that contains the given SSA variable’s definition.

        Since SSA variables can only be defined once, this will return the single instruction
        where that occurs. For SSA variable version 0s, which don’t have definitions, this will
        return None instead.

        Parameters:
        :   **ssa_var** ([*SSAVariable*](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable
            "binaryninja.mediumlevelil.SSAVariable") *|*
            [*HighLevelILVarSsa*](#binaryninja.highlevelil.HighLevelILVarSsa
            "binaryninja.highlevelil.HighLevelILVarSsa")) –

        Return type:
        :   [*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction") | *None*

    get_ssa_var_uses(*ssa_var: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [HighLevelILVarSsa](#binaryninja.highlevelil.HighLevelILVarSsa "binaryninja.highlevelil.HighLevelILVarSsa")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_ssa_var_uses)
    :   Gets all the instructions that use the given SSA variable.

        Parameters:
        :   **ssa_var** ([*SSAVariable*](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable
            "binaryninja.mediumlevelil.SSAVariable") *|*
            [*HighLevelILVarSsa*](#binaryninja.highlevelil.HighLevelILVarSsa
            "binaryninja.highlevelil.HighLevelILVarSsa")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction")]

    get_var_definitions(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_var_definitions)
    :   Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction")]

    get_var_uses(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")][[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.get_var_uses)
    :   Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) –

        Return type:
        :   [*List*](https://docs.python.org/3/library/typing.html#typing.List "(in Python
            v3.14)")[[*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction")]

    goto(*target: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.goto)
    :   `goto` unconditionally branch to a label

        Parameters:
        :   - **target** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – target of the goto
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `goto(target)`

        Return type:
        :   ExpressionIndex

    if_expr(*condition: ExpressionIndex*, *true_expr: ExpressionIndex*, *false_expr: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.if_expr)
    :   `if_expr` an if-statement expression with a condition and true/false branches. An `else`
        statement is included if the false_expr is not a NOP expression

        Parameters:
        :   - **condition** (*ExpressionIndex*) – expression for the condition to test
            - **true_expr** (*ExpressionIndex*) – expression for the true branch
            - **false_expr** (*ExpressionIndex*) – expression for the false branch
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `if (condition) { true_expr } else { false_expr }`

        Return type:
        :   ExpressionIndex

    imported_address(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.imported_address)
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

    int_to_float(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.int_to_float)
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

    intrinsic(*intrinsic: IntrinsicName | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | IntrinsicIndex*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.intrinsic)
    :   `intrinsic` return an intrinsic expression.

        Parameters:
        :   - **intrinsic** (*IntrinsicType*) – which intrinsic to call
            - **params** (*List**[**ExpressionIndex**]*) – parameters to intrinsic
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   an intrinsic expression.

        Return type:
        :   ExpressionIndex

    is_ssa_var_live(*ssa_var: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.is_ssa_var_live)
    :   `is_ssa_var_live` determines if `ssa_var` is live at any point in the function

        Parameters:
        :   **ssa_var** ([*SSAVariable*](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable
            "binaryninja.mediumlevelil.SSAVariable")) – the SSA variable to query

        Returns:
        :   whether the variable is live at any point in the function

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_ssa_var_live_at(*ssa_var: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*, *instr: InstructionIndex*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.is_ssa_var_live_at)
    :   `is_ssa_var_live_at` determines if `ssa_var` is live at a given point in the function;
        counts phi’s as uses

        Parameters:
        :   - **ssa_var** ([*SSAVariable*](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable
              "binaryninja.mediumlevelil.SSAVariable")) –
            - **instr** (*InstructionIndex*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is_var_live_at(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *instr: InstructionIndex*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.is_var_live_at)
    :   `is_var_live_at` determines if `var` is live at a given point in the function

        Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) –
            - **instr** (*InstructionIndex*) –

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    jump(*dest: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.jump)
    :   `jump` unconditionally branch to an expression by value

        Parameters:
        :   - **dest** (*ExpressionIndex*) – target of the jump
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `jump(dest)`

        Return type:
        :   ExpressionIndex

    label(*target: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.label)
    :   `label` create a label expression at a target

        Parameters:
        :   - **target** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – target of the label
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `target:`

        Return type:
        :   ExpressionIndex

    logical_shift_right(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.logical_shift_right)
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

    low_part(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.low_part)
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

    mod_double_prec_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.mod_double_prec_signed)
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

    mod_double_prec_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.mod_double_prec_unsigned)
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

    mod_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.mod_signed)
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

    mod_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.mod_unsigned)
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

    mult(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.mult)
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

    mult_double_prec_signed(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.mult_double_prec_signed)
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

    mult_double_prec_unsigned(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.mult_double_prec_unsigned)
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

    neg_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.neg_expr)
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

    no_ret(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.no_ret)
    :   `no_ret` returns an expression that halts execution

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `noreturn`

        Return type:
        :   ExpressionIndex

    nop(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.nop)
    :   `nop` no operation, this instruction does nothing

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – Location of expression

        Returns:
        :   The no operation expression

        Return type:
        :   ExpressionIndex

    not_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.not_expr)
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

    or_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.or_expr)
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

    remove_derived_string_reference_for_expr(*expr: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | ExpressionIndex | InstructionIndex*)[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.remove_derived_string_reference_for_expr)
    :   Parameters:
        :   **expr** ([*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction") *|* *ExpressionIndex* *|*
            *InstructionIndex*) –

    replace_expr(*original: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | ExpressionIndex | InstructionIndex*, *new: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | ExpressionIndex | InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.replace_expr)
    :   `replace_expr` allows modification of HLIL expressions

        Parameters:
        :   - **original** (*ExpressionIndex*) – the ExpressionIndex to replace (may also be an
              expression index)
            - **new** (*ExpressionIndex*) – the ExpressionIndex to add to the current
              HighLevelILFunction (may also be an expression index)

        Return type:
        :   *None*

    ret(*sources: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.ret)
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

    rotate_left(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.rotate_left)
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

    rotate_left_carry(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.rotate_left_carry)
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

    rotate_right(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.rotate_right)
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

    rotate_right_carry(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.rotate_right_carry)
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

    round_to_int(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.round_to_int)
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

    set_current_address(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *arch: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.set_current_address)
    :   Parameters:
        :   - **value** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –
            - **arch** ([*Architecture*](architecture.md#binaryninja.architecture.Architecture
              "binaryninja.architecture.Architecture") *|* *None*) –

        Return type:
        :   *None*

    set_derived_string_reference_for_expr(*expr: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | ExpressionIndex | InstructionIndex*, *str: [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString")*)[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.set_derived_string_reference_for_expr)
    :   Parameters:
        :   - **expr** ([*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction") *|* *ExpressionIndex* *|*
              *InstructionIndex*) –
            - **str** ([*DerivedString*](binaryview.md#binaryninja.binaryview.DerivedString
              "binaryninja.binaryview.DerivedString")) –

    set_expr_attributes(*expr: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | ExpressionIndex | InstructionIndex*, *value: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ILInstructionAttribute](enums.md#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[ILInstructionAttribute](enums.md#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute")]*)[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.set_expr_attributes)
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

    set_expr_type(*expr_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *expr_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [TypeBuilder](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.set_expr_type)
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
              [*TypeBuilder*](types.md#binaryninja.types.TypeBuilder "binaryninja.types.TypeBuilder"))
              –

        Return type:
        :   *None*

    shift_left(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.shift_left)
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

    sign_extend(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.sign_extend)
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

    split(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *hi: ExpressionIndex*, *lo: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.split)
    :   `var_split` combines expressions `hi` and `lo` of size `size` into an expression of size
        `2*size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of each expression in bytes
            - **hi** (*ExpressionIndex*) – the expression holding high part of value
            - **lo** (*ExpressionIndex*) – the expression holding low part of value
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `hi:lo`

        Return type:
        :   ExpressionIndex

    struct_field(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: ExpressionIndex*, *offset: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *member_index: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.struct_field)
    :   `struct_field` returns the structure field at offset `offset` and index `member_index`
        from expression `src` of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – the size of the field in bytes
            - **src** (*ExpressionIndex*) – the expression being read
            - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – offset of field in the structure
            - **member_index** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
              Python v3.14)")) – index of field in the structure
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `src:offset.size`

        Return type:
        :   ExpressionIndex

    sub(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.sub)
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

    sub_borrow(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *carry: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.sub_borrow)
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

    switch(*condition: ExpressionIndex*, *default_expr: ExpressionIndex*, *cases: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.switch)
    :   `switch` a switch expression with a condition, cases, and default case

        Parameters:
        :   - **condition** (*ExpressionIndex*) – expression for the switch condition
            - **default_expr** (*ExpressionIndex*) – expression for the default branch
            - **cases** (*List**[**ExpressionIndex**]*) – list of expressions for the switch cases
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `switch (condition) { cases...: ... default: default_expr }`

        Return type:
        :   ExpressionIndex

    system_call(*params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.system_call)
    :   `system_call` returns an expression which performs a system call with the parameters
        defined in `params`

        Parameters:
        :   - **params** (*List**[**ExpressionIndex**]*) – parameter variables
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `syscall(dest, params...)`

        Return type:
        :   ExpressionIndex

    tailcall(*dest: ExpressionIndex*, *params: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.tailcall)
    :   `tailcall` returns an expression which tailcalls the function in the expression `dest`
        with the parameters defined in `params`

        Parameters:
        :   - **dest** (*ExpressionIndex*) – the expression to call
            - **params** (*List**[**ExpressionIndex**]*) – parameter variables
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `tailcall(dest, params...)`

        Return type:
        :   ExpressionIndex

    test_bit(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.test_bit)
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

    trap(*value: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.trap)
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

    traverse(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, **args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, ***kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.traverse)
    :   `traverse` iterates through all the instructions in the HighLevelILFunction and calls
        the callback function for each instruction and sub-instruction. See the [Developer
        Docs](https://docs.binary.ninja/dev/concepts.html#walking-ils) for more examples.

        Parameters:
        :   - **cb** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in
              Python
              v3.14)")*[**[*[*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")*,*
              [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
              v3.14)")*]**,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")*]*) – The callback function to call for each node in the
              HighLevelILInstruction
            - **args** (*Any*) – Custom user-defined arguments
            - **kwargs** (*Any*) – Custom user-defined keyword arguments
            - **cb** –

        Returns:
        :   An iterator of the results of the callback function

        Return type:
        :   *Iterator*[*Any*]

        Example:
        :   ```
            >>> # find all calls to memcpy where the third parameter is not a constant
            >>> def find_non_constant_memcpy(i, target) -> HighLevelILInstruction:
            ...     match i:
            ...             case Localcall(dest=Constant(constant=c), params=[_, _, p]) if c == target and not isinstance(p, Constant):
            ...                     return i
            >>> target_address = bv.get_symbol_by_raw_name('_memcpy').address
            >>> for result in current_il_function.traverse(find_non_constant_memcpy, target_address):
            ...     print(f"Found suspicious memcpy: {repr(i)}")
            ```

    undefined(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.undefined)
    :   `undefined` returns the undefined expression. This should be used for instructions which
        perform functions but aren’t important for dataflow or partial emulation purposes.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the undefined expression.

        Return type:
        :   ExpressionIndex

    unimplemented(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.unimplemented)
    :   `unimplemented` returns the unimplemented expression. This should be used for all
        instructions which aren’t implemented.

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   the unimplemented expression.

        Return type:
        :   ExpressionIndex

    unimplemented_memory_ref(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *addr: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.unimplemented_memory_ref)
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

    unreachable(*loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.unreachable)
    :   `unreachable` returns an expression that is unreachable and should be omitted during
        analysis

        Parameters:
        :   **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
            "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `unreachable`

        Return type:
        :   ExpressionIndex

    var(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *src: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.var)
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

    var_declare(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.var_declare)
    :   `var_declare` declare a variable in the current scope

        Parameters:
        :   - **var** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – location of variable being declared
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `var` (no assignment or anything)

        Return type:
        :   ExpressionIndex

    var_init(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *dest: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*, *src: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.var_init)
    :   `var_init` declare and assign a variable in the current scope of size `size`

        Parameters:
        :   - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) – size of the variable
            - **dest** ([*Variable*](variable.md#binaryninja.variable.Variable
              "binaryninja.variable.Variable")) – location of variable being declared
            - **src** (*ExpressionIndex*) – value being assigned to the variable
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `dest = src`

        Return type:
        :   ExpressionIndex

    visit(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.visit)
    :   Iterates over all the instructions in the function and calls the callback function for
        each instruction and each sub-instruction.

        Parameters:
        :   **cb** (*HighLevelILVisitorCallback*) – Callback function that takes the name of the
            operand, the operand, operand type, and parent instruction

        Returns:
        :   True if all instructions were visited, False if the callback function returned False.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`HighLevelILFunction.traverse`](#binaryninja.highlevelil.HighLevelILFunction.traverse
        "binaryninja.highlevelil.HighLevelILFunction.traverse") instead.

    visit_all(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.visit_all)
    :   Iterates over all the instructions in the function and calls the callback function for
        each instruction and their operands.

        Parameters:
        :   **cb** (*HighLevelILVisitorCallback*) – Callback function that takes the name of the
            operand, the operand, operand type, and parent instruction

        Returns:
        :   True if all instructions were visited, False if the callback function returned False.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`HighLevelILFunction.traverse`](#binaryninja.highlevelil.HighLevelILFunction.traverse
        "binaryninja.highlevelil.HighLevelILFunction.traverse") instead.

    visit_operands(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.visit_operands)
    :   Iterates over all the instructions in the function and calls the callback function for each operand and
        :   the operands of each sub-instruction.

        Parameters:
        :   **cb** (*HighLevelILVisitorCallback*) – Callback function that takes the name of the
            operand, the operand, operand type, and parent instruction

        Returns:
        :   True if all instructions were visited, False if the callback function returned False.

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`HighLevelILFunction.traverse`](#binaryninja.highlevelil.HighLevelILFunction.traverse
        "binaryninja.highlevelil.HighLevelILFunction.traverse") instead.

    while_expr(*condition: ExpressionIndex*, *loop_expr: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.while_expr)
    :   `while_expr` a while-loop expression with a condition and loop body.

        Parameters:
        :   - **condition** (*ExpressionIndex*) – expression for the loop condition
            - **loop_expr** (*ExpressionIndex*) – expression for the loop body
            - **loc** ([*ILSourceLocation*](commonil.md#binaryninja.commonil.ILSourceLocation
              "binaryninja.commonil.ILSourceLocation")) – location of returned expression

        Returns:
        :   The expression `while (condition) { loop_expr }`

        Return type:
        :   ExpressionIndex

    xor_expr(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *a: ExpressionIndex*, *b: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.xor_expr)
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

    zero_extend(*size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *value: ExpressionIndex*, *loc: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → ExpressionIndex[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILFunction.zero_extend)
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
        also wish to consider HighLevelIlFunction.vars and
        HighLevelIlFunction.source_function.parameter_vars

    *property* arch*: [Architecture](architecture.md#binaryninja.architecture.Architecture "binaryninja.architecture.Architecture")*

    *property* basic_blocks*: [HighLevelILBasicBlockList](function.md#binaryninja.function.HighLevelILBasicBlockList "binaryninja.function.HighLevelILBasicBlockList")*

    *property* current_address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Current IL Address (read/write)

    *property* il_form*: [FunctionGraphType](enums.md#binaryninja.enums.FunctionGraphType "binaryninja.enums.FunctionGraphType")*

    *property* instructions*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   A generator of hlil instructions of the current function

    *property* medium_level_il*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Medium level IL for this function

    *property* mlil*: [MediumLevelILFunction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILFunction "binaryninja.mediumlevelil.MediumLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Alias for medium_level_il

    *property* non_ssa_form*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   High level IL in non-SSA (default) form (read-only)

    *property* root*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Root of the abstract syntax tree

    *property* source_function*: [Function](function.md#binaryninja.function.Function "binaryninja.function.Function")*

    *property* ssa_form*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*
    :   High level IL in SSA form (read-only)

    *property* ssa_vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   This gets just the HLIL SSA variables - you may be interested in the union of
        HighLevelIlFunction.source_function.parameter_vars and HighLevelIlFunction.aliased_vars
        for all the variables used in the function

    *property* vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*
    :   This gets just the HLIL variables - you may be interested in the union of
        HighLevelIlFunction.source_function.parameter_vars and HighLevelIlFunction.aliased_vars
        as well for all the variables used in the function

    *property* view*: [BinaryView](binaryview.md#binaryninja.binaryview.BinaryView "binaryninja.binaryview.BinaryView")*

## HighLevelILGoto

*class* HighLevelILGoto[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILGoto)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    HighLevelILGoto(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* target*: [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel")*

## HighLevelILIf

*class* HighLevelILIf[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILIf)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`ControlFlow`](commonil.md#binaryninja.commonil.ControlFlow
    "binaryninja.commonil.ControlFlow")

    HighLevelILIf(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* condition*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    *property* false*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* true*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILImport

*class* HighLevelILImport[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILImport)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Constant`](commonil.md#binaryninja.commonil.Constant "binaryninja.commonil.Constant")

    HighLevelILImport(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* constant*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILInstruction

*class* HighLevelILInstruction[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction)
:   Bases: [`BaseILInstruction`](commonil.md#binaryninja.commonil.BaseILInstruction
    "binaryninja.commonil.BaseILInstruction")

    `class HighLevelILInstruction` High Level Intermediate Language Instructions form an
    abstract syntax tree of the code. Control flow structures are present as high level
    constructs in the HLIL tree.

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    *classmethod* create(*func: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *instr_index: InstructionIndex | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.create)
    :   Parameters:
        :   - **func** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex* *|* *None*) –

        Return type:
        :   [*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
            "binaryninja.highlevelil.HighLevelILInstruction")

    get_instruction_hash(*discriminator: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.get_instruction_hash)
    :   Hash of instruction matching the C++ HighLevelILInstruction::GetInstructionHash, used
        for collapsed region matching. :param discriminator: Extra value to include in the hash
        to differentiate regions

        Parameters:
        :   **discriminator** ([*int*](https://docs.python.org/3/library/functions.html#int "(in
            Python v3.14)")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    get_lines(*settings: [DisassemblySettings](function.md#binaryninja.function.DisassemblySettings "binaryninja.function.DisassemblySettings") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.get_lines)
    :   Gets HLIL text lines with optional settings

        Parameters:
        :   **settings**
            ([*DisassemblySettings*](function.md#binaryninja.function.DisassemblySettings
            "binaryninja.function.DisassemblySettings") *|* *None*) –

        Return type:
        :   [*Generator*](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python
            v3.14)")[[*DisassemblyTextLine*](function.md#binaryninja.function.DisassemblyTextLine
            "binaryninja.function.DisassemblyTextLine"), *None*, *None*]

    get_possible_values(*options: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[DataFlowQueryOption](enums.md#binaryninja.enums.DataFlowQueryOption "binaryninja.enums.DataFlowQueryOption")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.get_possible_values)
    :   Parameters:
        :   **options** ([*List*](https://docs.python.org/3/library/typing.html#typing.List "(in
            Python v3.14)")*[*[*DataFlowQueryOption*](enums.md#binaryninja.enums.DataFlowQueryOption
            "binaryninja.enums.DataFlowQueryOption")*]* *|* *None*) –

        Return type:
        :   [*PossibleValueSet*](variable.md#binaryninja.variable.PossibleValueSet
            "binaryninja.variable.PossibleValueSet")

    get_ssa_var_version(*var: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*) → [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.get_ssa_var_version)
    :   Parameters:
        :   **var** ([*Variable*](variable.md#binaryninja.variable.Variable
            "binaryninja.variable.Variable")) –

        Return type:
        :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    *static* show_hlil_hierarchy()[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.show_hlil_hierarchy)
    :   Opens a new tab showing the HLIL hierarchy which includes classes which can easily be
        used with isinstance to match multiple types of IL instructions.

    traverse(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, **args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *shallow: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, ***kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*) → [Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.traverse)
    :   `traverse` is a generator that allows you to traverse the HLIL AST in a depth-first
        manner. It will yield the result of the callback function for each node in the AST.
        Arguments can be passed to the callback function using `args` and `kwargs`. See the
        [Developer Docs](https://docs.binary.ninja/dev/concepts.html#walking-ils) for more
        examples.

        Parameters:
        :   - **cb** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in
              Python
              v3.14)")*[**[*[*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction")*,*
              [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in Python
              v3.14)")*]**,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any "(in
              Python v3.14)")*]*) – The callback function to call for each node in the
              HighLevelILInstruction
            - **args** (*Any*) – Custom user-defined arguments
            - **shallow** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) – Whether traversal occurs on block instructions
            - **kwargs** (*Any*) – Custom user-defined keyword arguments
            - **cb** –

        Returns:
        :   An iterator of the results of the callback function

        Return type:
        :   *Iterator*[*Any*]

        Example:
        :   ```
            >>> def get_constant_less_than_value(inst: HighLevelILInstruction, value: int) -> int:
            ...     if isinstance(inst, Constant) and inst.constant < value:
            ...             return inst.constant
            >>>
            >>> for result in inst.traverse(get_constant_less_than_value, 10):
            ...     print(f"Found a constant {result} < 10 in {repr(inst)}")
            ```

        Example:
        :   ```
            >>> def get_import_data_var_with_name(inst: HighLevelILInstruction, name: str) -> Optional['DataVariable']:
            ...     if isinstance(inst, HighLevelILImport):
            ...                     if bv.get_symbol_at(inst.constant).name == name:
            ...                     return bv.get_data_var_at(inst.constant)
            >>>
            >>> for result in inst.traverse(get_import_data_var_with_name, "__cxa_finalize", shallow=False):
            ...     print(f"Found import at {result} in {repr(inst)}")
            ```

    visit(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'root'*, *parent: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.visit)
    :   Visits all HighLevelILInstructions in the operands of this instruction and any
        sub-instructions. In the callback you provide, you likely only need to interact with the
        second argument (see the example below).

        Parameters:
        :   - **cb** (*HighLevelILVisitorCallback*) – Callback function that takes the name of the
              operand, the operand, operand type, and parent instruction
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **parent** ([*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction") *|* *None*) –

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
            >>> for inst in bv.hlil_instructions:
            >>>     inst.visit(visitor)
            ```

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`HighLevelILInstruction.traverse`](#binaryninja.highlevelil.HighLevelILInstruction.traverse
        "binaryninja.highlevelil.HighLevelILInstruction.traverse") instead.

    visit_all(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'root'*, *parent: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.visit_all)
    :   Visits all operands of this instruction and all operands of any sub-instructions. Using
        pre-order traversal.

        Parameters:
        :   - **cb** (*HighLevelILVisitorCallback*) – Callback function that takes the name of the
              operand, the operand, operand type, and parent instruction
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **parent** ([*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction") *|* *None*) –

        Returns:
        :   True if all instructions were visited, False if the callback returned False

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`HighLevelILInstruction.traverse`](#binaryninja.highlevelil.HighLevelILInstruction.traverse
        "binaryninja.highlevelil.HighLevelILInstruction.traverse") instead.

    visit_operands(*cb: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'root'*, *parent: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILInstruction.visit_operands)
    :   Visits all leaf operands of this instruction and any sub-instructions.

        Parameters:
        :   - **cb** (*HighLevelILVisitorCallback*) – Callback function that takes the name of the
              operand, the operand, operand type, and parent instruction
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python
              v3.14)")) –
            - **parent** ([*HighLevelILInstruction*](#binaryninja.highlevelil.HighLevelILInstruction
              "binaryninja.highlevelil.HighLevelILInstruction") *|* *None*) –

        Returns:
        :   True if all instructions were visited, False if the callback returned False

        Return type:
        :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

        Deprecated since version 4.0.4907: Use
        [`HighLevelILInstruction.traverse`](#binaryninja.highlevelil.HighLevelILInstruction.traverse
        "binaryninja.highlevelil.HighLevelILInstruction.traverse") instead.

    ILOperations*: [ClassVar](https://docs.python.org/3/library/typing.html#typing.ClassVar "(in Python v3.14)")[[Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[HighLevelILOperation](enums.md#binaryninja.enums.HighLevelILOperation "binaryninja.enums.HighLevelILOperation"), [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]]]* *= {HighLevelILOperation.HLIL_NOP: [], HighLevelILOperation.HLIL_BLOCK: [('body', 'expr_list')], HighLevelILOperation.HLIL_IF: [('condition', 'expr'), ('true', 'expr'), ('false', 'expr')], HighLevelILOperation.HLIL_WHILE: [('condition', 'expr'), ('body', 'expr')], HighLevelILOperation.HLIL_DO_WHILE: [('body', 'expr'), ('condition', 'expr')], HighLevelILOperation.HLIL_FOR: [('init', 'expr'), ('condition', 'expr'), ('update', 'expr'), ('body', 'expr')], HighLevelILOperation.HLIL_SWITCH: [('condition', 'expr'), ('default', 'expr'), ('cases', 'expr_list')], HighLevelILOperation.HLIL_CASE: [('values', 'expr_list'), ('body', 'expr')], HighLevelILOperation.HLIL_BREAK: [], HighLevelILOperation.HLIL_CONTINUE: [], HighLevelILOperation.HLIL_JUMP: [('dest', 'expr')], HighLevelILOperation.HLIL_RET: [('src', 'expr_list')], HighLevelILOperation.HLIL_NORET: [], HighLevelILOperation.HLIL_GOTO: [('target', 'label')], HighLevelILOperation.HLIL_LABEL: [('target', 'label')], HighLevelILOperation.HLIL_VAR_DECLARE: [('var', 'var')], HighLevelILOperation.HLIL_VAR_INIT: [('dest', 'var'), ('src', 'expr')], HighLevelILOperation.HLIL_ASSIGN: [('dest', 'expr'), ('src', 'expr')], HighLevelILOperation.HLIL_ASSIGN_UNPACK: [('dest', 'expr_list'), ('src', 'expr')], HighLevelILOperation.HLIL_VAR: [('var', 'var')], HighLevelILOperation.HLIL_STRUCT_FIELD: [('src', 'expr'), ('offset', 'int'), ('member_index', 'member_index')], HighLevelILOperation.HLIL_ARRAY_INDEX: [('src', 'expr'), ('index', 'expr')], HighLevelILOperation.HLIL_SPLIT: [('high', 'expr'), ('low', 'expr')], HighLevelILOperation.HLIL_DEREF: [('src', 'expr')], HighLevelILOperation.HLIL_DEREF_FIELD: [('src', 'expr'), ('offset', 'int'), ('member_index', 'member_index')], HighLevelILOperation.HLIL_ADDRESS_OF: [('src', 'expr')], HighLevelILOperation.HLIL_CONST: [('constant', 'int')], HighLevelILOperation.HLIL_CONST_DATA: [('constant', 'ConstantData')], HighLevelILOperation.HLIL_CONST_PTR: [('constant', 'int')], HighLevelILOperation.HLIL_EXTERN_PTR: [('constant', 'int'), ('offset', 'int')], HighLevelILOperation.HLIL_FLOAT_CONST: [('constant', 'float')], HighLevelILOperation.HLIL_IMPORT: [('constant', 'int')], HighLevelILOperation.HLIL_ADD: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_ADC: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], HighLevelILOperation.HLIL_SUB: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_SBB: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], HighLevelILOperation.HLIL_AND: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_OR: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_XOR: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_LSL: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_LSR: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_ASR: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_ROL: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_RLC: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], HighLevelILOperation.HLIL_ROR: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_RRC: [('left', 'expr'), ('right', 'expr'), ('carry', 'expr')], HighLevelILOperation.HLIL_MUL: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_MULU_DP: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_MULS_DP: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_DIVU: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_DIVU_DP: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_DIVS: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_DIVS_DP: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_MODU: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_MODU_DP: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_MODS: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_MODS_DP: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_NEG: [('src', 'expr')], HighLevelILOperation.HLIL_NOT: [('src', 'expr')], HighLevelILOperation.HLIL_SX: [('src', 'expr')], HighLevelILOperation.HLIL_ZX: [('src', 'expr')], HighLevelILOperation.HLIL_LOW_PART: [('src', 'expr')], HighLevelILOperation.HLIL_CALL: [('dest', 'expr'), ('params', 'expr_list')], HighLevelILOperation.HLIL_CMP_E: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_CMP_NE: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_CMP_SLT: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_CMP_ULT: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_CMP_SLE: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_CMP_ULE: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_CMP_SGE: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_CMP_UGE: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_CMP_SGT: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_CMP_UGT: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_TEST_BIT: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_BOOL_TO_INT: [('src', 'expr')], HighLevelILOperation.HLIL_ADD_OVERFLOW: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_SYSCALL: [('params', 'expr_list')], HighLevelILOperation.HLIL_TAILCALL: [('dest', 'expr'), ('params', 'expr_list')], HighLevelILOperation.HLIL_INTRINSIC: [('intrinsic', 'intrinsic'), ('params', 'expr_list')], HighLevelILOperation.HLIL_BP: [], HighLevelILOperation.HLIL_TRAP: [('vector', 'int')], HighLevelILOperation.HLIL_UNDEF: [], HighLevelILOperation.HLIL_UNIMPL: [], HighLevelILOperation.HLIL_UNIMPL_MEM: [('src', 'expr')], HighLevelILOperation.HLIL_FADD: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FSUB: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FMUL: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FDIV: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FSQRT: [('src', 'expr')], HighLevelILOperation.HLIL_FNEG: [('src', 'expr')], HighLevelILOperation.HLIL_FABS: [('src', 'expr')], HighLevelILOperation.HLIL_FLOAT_TO_INT: [('src', 'expr')], HighLevelILOperation.HLIL_INT_TO_FLOAT: [('src', 'expr')], HighLevelILOperation.HLIL_FLOAT_CONV: [('src', 'expr')], HighLevelILOperation.HLIL_ROUND_TO_INT: [('src', 'expr')], HighLevelILOperation.HLIL_FLOOR: [('src', 'expr')], HighLevelILOperation.HLIL_CEIL: [('src', 'expr')], HighLevelILOperation.HLIL_FTRUNC: [('src', 'expr')], HighLevelILOperation.HLIL_FCMP_E: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FCMP_NE: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FCMP_LT: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FCMP_LE: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FCMP_GE: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FCMP_GT: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FCMP_O: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_FCMP_UO: [('left', 'expr'), ('right', 'expr')], HighLevelILOperation.HLIL_UNREACHABLE: [], HighLevelILOperation.HLIL_WHILE_SSA: [('condition_phi', 'expr'), ('condition', 'expr'), ('body', 'expr')], HighLevelILOperation.HLIL_DO_WHILE_SSA: [('body', 'expr'), ('condition_phi', 'expr'), ('condition', 'expr')], HighLevelILOperation.HLIL_FOR_SSA: [('init', 'expr'), ('condition_phi', 'expr'), ('condition', 'expr'), ('update', 'expr'), ('body', 'expr')], HighLevelILOperation.HLIL_VAR_INIT_SSA: [('dest', 'var_ssa'), ('src', 'expr')], HighLevelILOperation.HLIL_ASSIGN_MEM_SSA: [('dest', 'expr'), ('dest_memory', 'int'), ('src', 'expr'), ('src_memory', 'int')], HighLevelILOperation.HLIL_ASSIGN_UNPACK_MEM_SSA: [('dest', 'expr_list'), ('dest_memory', 'int'), ('src', 'expr'), ('src_memory', 'int')], HighLevelILOperation.HLIL_VAR_SSA: [('var', 'var_ssa')], HighLevelILOperation.HLIL_ARRAY_INDEX_SSA: [('src', 'expr'), ('src_memory', 'int'), ('index', 'expr')], HighLevelILOperation.HLIL_DEREF_SSA: [('src', 'expr'), ('src_memory', 'int')], HighLevelILOperation.HLIL_DEREF_FIELD_SSA: [('src', 'expr'), ('src_memory', 'int'), ('offset', 'int'), ('member_index', 'member_index')], HighLevelILOperation.HLIL_CALL_SSA: [('dest', 'expr'), ('params', 'expr_list'), ('dest_memory', 'int'), ('src_memory', 'int')], HighLevelILOperation.HLIL_SYSCALL_SSA: [('params', 'expr_list'), ('dest_memory', 'int'), ('src_memory', 'int')], HighLevelILOperation.HLIL_INTRINSIC_SSA: [('intrinsic', 'intrinsic'), ('params', 'expr_list'), ('dest_memory', 'int'), ('src_memory', 'int')], HighLevelILOperation.HLIL_VAR_PHI: [('dest', 'var_ssa'), ('src', 'var_ssa_list')], HighLevelILOperation.HLIL_MEM_PHI: [('dest', 'int'), ('src', 'int_list')]}*

    *property* address*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* ast*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*
    :   This expression with full AST printing (read-only)

    *property* attributes*: [Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[ILInstructionAttribute](enums.md#binaryninja.enums.ILInstructionAttribute "binaryninja.enums.ILInstructionAttribute")]*
    :   The set of optional attributes placed on the instruction

    *property* can_collapse*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*
    :   If this instruction can be collapsed in rendered lines

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* core_operands*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*

    *property* derived_string_reference*: [DerivedString](binaryview.md#binaryninja.binaryview.DerivedString "binaryninja.binaryview.DerivedString") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    *property* expr_type*: [Type](types.md#binaryninja.types.Type "binaryninja.types.Type") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Type of expression

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    *property* has_side_effects*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* il_basic_block*: [HighLevelILBasicBlock](#binaryninja.highlevelil.HighLevelILBasicBlock "binaryninja.highlevelil.HighLevelILBasicBlock") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   IL basic block object containing this expression (read-only) (only available on
        finalized functions). Returns None for HLIL_BLOCK expressions as these can contain
        multiple basic blocks.

    *property* instr*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*
    :   The statement that this expression belongs to (read-only)

    instr_index*: InstructionIndex*

    *property* instruction_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    *property* lines*: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[DisassemblyTextLine](function.md#binaryninja.function.DisassemblyTextLine "binaryninja.function.DisassemblyTextLine"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*
    :   HLIL text lines (read-only)

    *property* llil*: [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Alias for low_level_il

    *property* llils*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[ExpressionIndex]*

    *property* low_level_il*: [LowLevelILInstruction](lowlevelil.md#binaryninja.lowlevelil.LowLevelILInstruction "binaryninja.lowlevelil.LowLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Low level IL form of this expression

    *property* medium_level_il*: [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Medium level IL form of this expression

    *property* mlil*: [MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Alias for medium_level_il

    *property* mlils*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[MediumLevelILInstruction](mediumlevelil.md#binaryninja.mediumlevelil.MediumLevelILInstruction "binaryninja.mediumlevelil.MediumLevelILInstruction")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* non_ast*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*
    :   This expression without full AST printing (read-only)

    *property* non_ssa_form*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*
    :   Non-SSA form of expression (read-only)

    *property* operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer")]*
    :   Operands for the instruction

        Consider using more specific APIs for `src`, `dest`, `params`, etc where appropriate.

    *property* operation*: [HighLevelILOperation](enums.md#binaryninja.enums.HighLevelILOperation "binaryninja.enums.HighLevelILOperation")*

    *property* parent*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* possible_values*: [PossibleValueSet](variable.md#binaryninja.variable.PossibleValueSet "binaryninja.variable.PossibleValueSet")*
    :   Possible values of expression using path-sensitive static data flow analysis (read-only)

    *property* postfix_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") | [HighLevelILOperationAndSize](#binaryninja.highlevelil.HighLevelILOperationAndSize "binaryninja.highlevelil.HighLevelILOperationAndSize")]*
    :   All operands in the expression tree in postfix order

    *property* prefix_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer") | [HighLevelILOperationAndSize](#binaryninja.highlevelil.HighLevelILOperationAndSize "binaryninja.highlevelil.HighLevelILOperationAndSize")]*
    :   All operands in the expression tree in prefix order

    *property* raw_operands*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex, ExpressionIndex]*
    :   Raw operand expression indices as specified by the core structure (read-only)

    *property* size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* source_location*: [ILSourceLocation](commonil.md#binaryninja.commonil.ILSourceLocation "binaryninja.commonil.ILSourceLocation")*

    *property* source_operand*: ExpressionIndex*

    *property* ssa_form*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*
    :   SSA form of expression (read-only)

    *property* ssa_memory_version*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*
    :   Version of active memory contents in SSA form for this instruction

    *property* tokens*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[InstructionTextToken](architecture.md#binaryninja.architecture.InstructionTextToken "binaryninja.architecture.InstructionTextToken")]*
    :   HLIL tokens taken from the HLIL text lines (read-only) – does not include newlines or
        indentation, use lines for that information

    *property* value*: [RegisterValue](variable.md#binaryninja.variable.RegisterValue "binaryninja.variable.RegisterValue")*
    :   Value of expression if constant or a known value (read-only)

    *property* vars*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   Non-unique list of variables read by instruction

    *property* vars_address_taken*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   Non-unique list of variables whose address is taken by instruction

        Note

        This property has some nuance to it, so use carefully. This property will return only
        those variable which directly have their address taken such as &var_4 or &var_8.d but
        not those which are involved in an address calculation such as &(var_4 + 0) or &var_4[0]
        even though they may be functionally equivalent.

    *property* vars_read*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   Non-unique list of variables whose value is read by this instruction

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables value is written by this instruction

## HighLevelILIntToFloat

*class* HighLevelILIntToFloat[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILIntToFloat)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILIntToFloat(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILIntrinsic

*class* HighLevelILIntrinsic[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILIntrinsic)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Intrinsic`](commonil.md#binaryninja.commonil.Intrinsic
    "binaryninja.commonil.Intrinsic")

    HighLevelILIntrinsic(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* intrinsic*: [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

## HighLevelILIntrinsicSsa

*class* HighLevelILIntrinsicSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILIntrinsicSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILIntrinsicSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* intrinsic*: [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic")*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILJump

*class* HighLevelILJump[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILJump)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    HighLevelILJump(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILLabel

*class* HighLevelILLabel[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILLabel)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILLabel(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* target*: [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel")*

## HighLevelILLowPart

*class* HighLevelILLowPart[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILLowPart)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILLowPart(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILLsl

*class* HighLevelILLsl[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILLsl)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILLsl(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILLsr

*class* HighLevelILLsr[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILLsr)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILLsr(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILMemPhi

*class* HighLevelILMemPhi[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILMemPhi)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Memory`](commonil.md#binaryninja.commonil.Memory "binaryninja.commonil.Memory"),
    [`Phi`](commonil.md#binaryninja.commonil.Phi "binaryninja.commonil.Phi")

    HighLevelILMemPhi(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*

## HighLevelILMods

*class* HighLevelILMods[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILMods)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed")

    HighLevelILMods(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILModsDp

*class* HighLevelILModsDp[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILModsDp)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Signed`](commonil.md#binaryninja.commonil.Signed "binaryninja.commonil.Signed"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    HighLevelILModsDp(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILModu

*class* HighLevelILModu[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILModu)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILModu(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILModuDp

*class* HighLevelILModuDp[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILModuDp)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    HighLevelILModuDp(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILMul

*class* HighLevelILMul[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILMul)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILMul(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILMulsDp

*class* HighLevelILMulsDp[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILMulsDp)
:   Bases: [`Signed`](commonil.md#binaryninja.commonil.Signed
    "binaryninja.commonil.Signed"),
    [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    HighLevelILMulsDp(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILMuluDp

*class* HighLevelILMuluDp[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILMuluDp)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`DoublePrecision`](commonil.md#binaryninja.commonil.DoublePrecision
    "binaryninja.commonil.DoublePrecision")

    HighLevelILMuluDp(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILNeg

*class* HighLevelILNeg[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILNeg)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILNeg(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILNop

*class* HighLevelILNop[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILNop)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILNop(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILNoret

*class* HighLevelILNoret[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILNoret)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    HighLevelILNoret(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILNot

*class* HighLevelILNot[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILNot)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILNot(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILOperationAndSize

*class* HighLevelILOperationAndSize[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILOperationAndSize)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python
    v3.14)")

    HighLevelILOperationAndSize(operation: binaryninja.enums.HighLevelILOperation, size:
    int)

    __init__(*operation: [HighLevelILOperation](enums.md#binaryninja.enums.HighLevelILOperation "binaryninja.enums.HighLevelILOperation")*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **operation** ([*HighLevelILOperation*](enums.md#binaryninja.enums.HighLevelILOperation
              "binaryninja.enums.HighLevelILOperation")) –
            - **size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python
              v3.14)")) –

        Return type:
        :   *None*

    operation*: [HighLevelILOperation](enums.md#binaryninja.enums.HighLevelILOperation "binaryninja.enums.HighLevelILOperation")*

    size*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILOr

*class* HighLevelILOr[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILOr)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILOr(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILRet

*class* HighLevelILRet[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILRet)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Return`](commonil.md#binaryninja.commonil.Return "binaryninja.commonil.Return")

    HighLevelILRet(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

## HighLevelILRlc

*class* HighLevelILRlc[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILRlc)
:   Bases: [`HighLevelILCarryBase`](#binaryninja.highlevelil.HighLevelILCarryBase
    "binaryninja.highlevelil.HighLevelILCarryBase")

    HighLevelILRlc(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILRol

*class* HighLevelILRol[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILRol)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILRol(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILRor

*class* HighLevelILRor[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILRor)
:   Bases: [`HighLevelILCarryBase`](#binaryninja.highlevelil.HighLevelILCarryBase
    "binaryninja.highlevelil.HighLevelILCarryBase")

    HighLevelILRor(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILRoundToInt

*class* HighLevelILRoundToInt[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILRoundToInt)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`FloatingPoint`](commonil.md#binaryninja.commonil.FloatingPoint
    "binaryninja.commonil.FloatingPoint")

    HighLevelILRoundToInt(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILRrc

*class* HighLevelILRrc[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILRrc)
:   Bases: [`HighLevelILCarryBase`](#binaryninja.highlevelil.HighLevelILCarryBase
    "binaryninja.highlevelil.HighLevelILCarryBase")

    HighLevelILRrc(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILSbb

*class* HighLevelILSbb[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILSbb)
:   Bases: [`HighLevelILCarryBase`](#binaryninja.highlevelil.HighLevelILCarryBase
    "binaryninja.highlevelil.HighLevelILCarryBase")

    HighLevelILSbb(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILSplit

*class* HighLevelILSplit[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILSplit)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILSplit(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    *property* high*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    instr_index*: InstructionIndex*

    *property* low*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILStructField

*class* HighLevelILStructField[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILStructField)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILStructField(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* member_index*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")*

    *property* offset*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILSub

*class* HighLevelILSub[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILSub)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILSub(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILSwitch

*class* HighLevelILSwitch[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILSwitch)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`ControlFlow`](commonil.md#binaryninja.commonil.ControlFlow
    "binaryninja.commonil.ControlFlow")

    HighLevelILSwitch(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* cases*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    *property* condition*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* default*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILSx

*class* HighLevelILSx[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILSx)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILSx(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILSyscall

*class* HighLevelILSyscall[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILSyscall)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Syscall`](commonil.md#binaryninja.commonil.Syscall "binaryninja.commonil.Syscall")

    HighLevelILSyscall(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

## HighLevelILSyscallSsa

*class* HighLevelILSyscallSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILSyscallSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Syscall`](commonil.md#binaryninja.commonil.Syscall "binaryninja.commonil.Syscall"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILSyscallSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

    *property* src_memory*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILTailcall

*class* HighLevelILTailcall[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILTailcall)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Tailcall`](commonil.md#binaryninja.commonil.Tailcall "binaryninja.commonil.Tailcall")

    HighLevelILTailcall(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* params*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")]*

## HighLevelILTestBit

*class* HighLevelILTestBit[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILTestBit)
:   Bases: [`HighLevelILComparisonBase`](#binaryninja.highlevelil.HighLevelILComparisonBase
    "binaryninja.highlevelil.HighLevelILComparisonBase")

    HighLevelILTestBit(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILTrap

*class* HighLevelILTrap[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILTrap)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    HighLevelILTrap(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* vector*: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*

## HighLevelILUnaryBase

*class* HighLevelILUnaryBase[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILUnaryBase)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`UnaryOperation`](commonil.md#binaryninja.commonil.UnaryOperation
    "binaryninja.commonil.UnaryOperation")

    HighLevelILUnaryBase(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

## HighLevelILUndef

*class* HighLevelILUndef[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILUndef)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    HighLevelILUndef(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILUnimpl

*class* HighLevelILUnimpl[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILUnimpl)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILUnimpl(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILUnimplMem

*class* HighLevelILUnimplMem[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILUnimplMem)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`Memory`](commonil.md#binaryninja.commonil.Memory "binaryninja.commonil.Memory")

    HighLevelILUnimplMem(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILUnreachable

*class* HighLevelILUnreachable[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILUnreachable)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Terminal`](commonil.md#binaryninja.commonil.Terminal "binaryninja.commonil.Terminal")

    HighLevelILUnreachable(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILVar

*class* HighLevelILVar[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILVar)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`VariableInstruction`](commonil.md#binaryninja.commonil.VariableInstruction
    "binaryninja.commonil.VariableInstruction")

    HighLevelILVar(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* var*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## HighLevelILVarDeclare

*class* HighLevelILVarDeclare[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILVarDeclare)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction")

    HighLevelILVarDeclare(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* var*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

## HighLevelILVarInit

*class* HighLevelILVarInit[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILVarInit)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar")

    HighLevelILVarInit(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables value is written by this instruction

## HighLevelILVarInitSsa

*class* HighLevelILVarInitSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILVarInitSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILVarInitSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables value is written by this instruction

## HighLevelILVarPhi

*class* HighLevelILVarPhi[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILVarPhi)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Phi`](commonil.md#binaryninja.commonil.Phi "binaryninja.commonil.Phi"),
    [`SetVar`](commonil.md#binaryninja.commonil.SetVar "binaryninja.commonil.SetVar")

    HighLevelILVarPhi(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* dest*: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* src*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")]*

    *property* vars_written*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")]*
    :   List of variables value is written by this instruction

## HighLevelILVarSsa

*class* HighLevelILVarSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILVarSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`SSAVariableInstruction`](commonil.md#binaryninja.commonil.SSAVariableInstruction
    "binaryninja.commonil.SSAVariableInstruction")

    HighLevelILVarSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

    *property* var*: [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")*

## HighLevelILWhile

*class* HighLevelILWhile[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILWhile)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Loop`](commonil.md#binaryninja.commonil.Loop "binaryninja.commonil.Loop")

    HighLevelILWhile(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* body*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* condition*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILWhileSsa

*class* HighLevelILWhileSsa[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILWhileSsa)
:   Bases: [`HighLevelILInstruction`](#binaryninja.highlevelil.HighLevelILInstruction
    "binaryninja.highlevelil.HighLevelILInstruction"),
    [`Loop`](commonil.md#binaryninja.commonil.Loop "binaryninja.commonil.Loop"),
    [`SSA`](commonil.md#binaryninja.commonil.SSA "binaryninja.commonil.SSA")

    HighLevelILWhileSsa(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    *property* body*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* condition*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    *property* condition_phi*: [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    *property* detailed_operands*: [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction") | [ILIntrinsic](lowlevelil.md#binaryninja.lowlevelil.ILIntrinsic "binaryninja.lowlevelil.ILIntrinsic") | [Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable") | [SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable") | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[Variable](variable.md#binaryninja.variable.Variable "binaryninja.variable.Variable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[SSAVariable](mediumlevelil.md#binaryninja.mediumlevelil.SSAVariable "binaryninja.mediumlevelil.SSAVariable")] | [List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[HighLevelILInstruction](#binaryninja.highlevelil.HighLevelILInstruction "binaryninja.highlevelil.HighLevelILInstruction")] | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [GotoLabel](#binaryninja.highlevelil.GotoLabel "binaryninja.highlevelil.GotoLabel") | [ConstantData](variable.md#binaryninja.variable.ConstantData "binaryninja.variable.ConstantData") | [DataBuffer](databuffer.md#binaryninja.databuffer.DataBuffer "binaryninja.databuffer.DataBuffer"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]*
    :   Returns a list of tuples containing the name of the operand, the operand, and the type
        of the operand. Useful for iterating over all operands of an instruction and
        sub-instructions.

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILXor

*class* HighLevelILXor[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILXor)
:   Bases: [`HighLevelILBinaryBase`](#binaryninja.highlevelil.HighLevelILBinaryBase
    "binaryninja.highlevelil.HighLevelILBinaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILXor(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*

## HighLevelILZx

*class* HighLevelILZx[[source]](https://api.binary.ninja/_modules/binaryninja/highlevelil.html#HighLevelILZx)
:   Bases: [`HighLevelILUnaryBase`](#binaryninja.highlevelil.HighLevelILUnaryBase
    "binaryninja.highlevelil.HighLevelILUnaryBase"),
    [`Arithmetic`](commonil.md#binaryninja.commonil.Arithmetic
    "binaryninja.commonil.Arithmetic")

    HighLevelILZx(function: ‘HighLevelILFunction’, expr_index: <function
    NewType.<locals>.new_type at 0x105107820>, core_instr:
    binaryninja.highlevelil.CoreHighLevelILInstruction, as_ast: bool, instr_index: <function
    NewType.<locals>.new_type at 0x105092940>)

    __init__(*function: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*, *expr_index: ExpressionIndex*, *core_instr: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*, *as_ast: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *instr_index: InstructionIndex*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Parameters:
        :   - **function** ([*HighLevelILFunction*](#binaryninja.highlevelil.HighLevelILFunction
              "binaryninja.highlevelil.HighLevelILFunction")) –
            - **expr_index** (*ExpressionIndex*) –
            - **core_instr**
              ([*CoreHighLevelILInstruction*](#binaryninja.highlevelil.CoreHighLevelILInstruction
              "binaryninja.highlevelil.CoreHighLevelILInstruction")) –
            - **as_ast** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python
              v3.14)")) –
            - **instr_index** (*InstructionIndex*) –

        Return type:
        :   *None*

    as_ast*: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*

    core_instr*: [CoreHighLevelILInstruction](#binaryninja.highlevelil.CoreHighLevelILInstruction "binaryninja.highlevelil.CoreHighLevelILInstruction")*

    expr_index*: ExpressionIndex*

    function*: [HighLevelILFunction](#binaryninja.highlevelil.HighLevelILFunction "binaryninja.highlevelil.HighLevelILFunction")*

    instr_index*: InstructionIndex*
