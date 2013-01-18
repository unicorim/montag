a := System args at(1)


if (a == "init") then (writeln("Initialized montag in " .. Directory currentWorkingDirectory)) elseif (a == "new") then (writeln("Initializing montag in " .. Directory currentWorkingDirectory .. "/" .. System args at(2) .. ". Please wait...") Directory setPath("/" .. System args at(2)) exists print) else (writeln "WUT are you talking about?") 
