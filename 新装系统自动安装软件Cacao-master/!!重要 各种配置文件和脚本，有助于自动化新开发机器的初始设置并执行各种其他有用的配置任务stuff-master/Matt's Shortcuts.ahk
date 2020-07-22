AppsKey::Send {AppsKey}
AppsKey & 1::Send #{1}
AppsKey & 2::Send #{2}
AppsKey & 3::Send #{3}
AppsKey & 4::Send #{4}
AppsKey & 5::Send #{5}
AppsKey & 6::Send #{6}
AppsKey & 7::Send #{7}
AppsKey & 8::Send #{8}
AppsKey & 9::Send #{9}
AppsKey & 0::Send #{0}

;old 5-button mouse macros, less useful now, commented out
;XButton2 & LButton::SendInput ^c
;XButton2 & RButton::SendInput ^v
;XButton2 & MButton::SendInput ^V
;XButton2 & XButton1::Send !{Tab}
;XButton2 & WheelUp::Send #{F11}
;XButton2 & WheelDown::Send #{F11}
;XButton1 & WheelDown::Send {Alt Down}{Tab}{Alt Up}
;XButton1 & XButton2::SendInput ^a doesn't work?
;XButton1 & WheelUp::Send !{ESC}
;XButton1 & WheelDown::Send !+{ESC} 
;~MButton & WheelUp::AltTab
;~MButton & WheelDown::ShiftAltTab
;~MButton & LButton::SendInput ^c
;~MButton & RButton::SendInput ^v

;swap caps and escape
$CapsLock::SendInput {Escape}
$Escape::SetCapsLockState Off

!#y::
{
    ;opens skype search
    Send ^!+3
    Send {Escape}
    return
}

#z::
{
    ; toggle skype mute
    Send #{F4}
    return
}


^Ins::
{
    Send ^c
}

:*:ssf::
(
SELECT	*
FROM	`
)

^!t::
FormatTime, TimeString,, yyyy-MM-dd HH:mm
Send %TimeString%
return


XButton1::
DllCall("SystemParametersInfo", Int,113, Int,0, UInt,3, Int,2)
KeyWait, XButton1
DllCall("SystemParametersInfo", Int,113, Int,0, UInt,10, Int,2)
return

XButton2::
DllCall("SystemParametersInfo", Int,113, Int,0, UInt,15, Int,2)
return
