yaml := Object clone do (
     read := method(this_file,
      f := File with(this_file) readLines
      f foreach(f, f println)
    )
  )

trial := yaml clone
trial read("foo.yaml")