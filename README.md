# Pymk

This is a set of Python functions that simplify building projects with the
power of a full programming language and the intuitive syntax of Python.

## Add it to your project

Copy the `mkpy` folder into your project and create a `pymk.py` file based on
the one available in this project.

Optionally include the lines of the `.gitignore` in this project into your
`.gitignore`.

## Use it

All procedures declared inside `pymk.py` can be called from the terminal if
their name is passed as argument. For example, in this project you can call

```
./pymk.py example_procedure 
```

By default the sample pymk.py file stores the last procedure called and this is
the one that will be called if you run `./pymk.py` without arguments.

The first time you call this pymk.py script it will prompt you with a command
that will install support for tab complete in these procedures. You can disable
tab completions (and silence the warning) by removing the call to
`handle_tab_complete()`.

## FAQ

**Q:** Why not use available build systems?

**A:** After trying several of them I think creating textual representations
that are "simpler" than a programming language is the wrong approach. They
become bloated systems with lots of configuration options, huge documentation
and a lot of magic behind the scenes. In the end, to provide maximum
flexibility, they either grow to be turing complete languages or provide a way
to call a real programming language like Bash. I'm starting the other way
around, start from a fully fledged programming language and symplify the common
tasks required to build a project.

##

**Q:** Why Python?

**A:** Mainly, because it's the scripting language I'm most familiar with and
has intuitive syntax. Also, it comes preinstalled in Linux (my main development
environment), has some degree of metaprogramming built in and is multiplatform.

##

**Q:** Why is it not a package installable with pip or other package manager?

**A:** I don't think it's the right release process for a build system. Making
the build code part of the project avoids adding an external dependency to the
installed version of the build tool. This has several advantages:

 - Someone building the project doesn't need a specific version of pymk, the
   one in the source should _just work_.

 - Building old revisions of the project becomes easier, because the build code
   is versioned together with the project's code.

 - There is no need to install Pymk, which is one step less in the build
   process.

 - Usually API compatibility won't break. But in case it does, changes in Pymk
   won't silently break the project build after a system update. These breaks
   will only happen when the project explicitly upgrades Pymk and hopefully
   they will be fixed at the same time.

 - Users can easily modify the internals of Pymk in case they don't work for
   them. Users get close to the implementation details of pymk.

##

**Q:** Can I have a pymk.py file in each subdirectory of my project?

**A:** No. I've usually seen this be more problematic than useful. It requires
choosing a policy about the base of relative paths, handling paths as different
entities (not just strings), and most likely will imply adding configuration
options to support all use cases. Still, nothing stops you from calling Python
scripts in other subdirectories. But, unlike other build systems, pymk hasn't
been designed around this paradigm.
