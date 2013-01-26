doFile("lib/yaml.io")

a := System args at(1)
b := System args at(2)

cmd := Object clone do (
  dir := Directory currentWorkingDirectory
  mod := method("Will put something else here okay?" println)

  boot := method(writeln("Initialized montag in " .. dir))
 )

arg := cmd clone
yender := yaml clone

if (a=="init") then (cmd boot) elseif (a=="make") then (yender write(b)) else ("WUT?" println)