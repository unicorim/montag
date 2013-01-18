a := System args at(1)
b := System args at(2)

cmd := Object clone do (
  dir := Directory currentWorkingDirectory
  mod := method("Will put something else here okay?" println)

  boot := method(writeln("Initialized montag in " .. dir))
  create := method(newly,
      	 writeln("Initializing montag in " .. dir .. "/" .. newly))
)

arg := cmd clone

if (a=="init", cmd boot) elseif (a=="new", cmd create(b), "WUT?" print)