yaml := Object clone do (
     read := method(this_file,
      f := File with(this_file) readLines
      f foreach(f, f println)
    )
     write := method(this_file,
      keywords := list("title", "author", "created", "content", "tags")
      f := File with(this_file) readLines
      i := File with(this_file .. ".mntg") remove openForUpdating
      f foreach(keywords, i write(keywords .. " : " .. f, "\n"))
    )
  )

trial := yaml clone
trial read("foo.txt")
trial write("foo.txt")
trial read("foo.txt.mntg")