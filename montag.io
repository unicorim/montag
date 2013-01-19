a := System args at(1)

cmd := Object clone do (
  dir := Directory currentWorkingDirectory
  mod := method("Will put something else here okay?" println)

  boot := method(writeln("Initialized montag in " .. dir))
)

arg := cmd clone

if (a=="init", cmd boot, "WUT?" println)