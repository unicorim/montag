yaml := Object clone do (
     read := method(this_file,
      f := File with(this_file) readLines
      f foreach(f, f println)
    )
     write := method(this_file,
      keywords := list("title", "author", "created", "content", "tags")
      f := File with(this_file) readLines as Mutable strip
      i := File with(this_file .. ".mntg") remove openForUpdating
      keywords foreach(k,e, i write(e .. ": " .. f at(k), "\n"))
    )
  )

trial := yaml clone
trial write("foo.txt")
trial read("foo.txt.mntg")