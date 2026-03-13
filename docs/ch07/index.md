# Chapter 7: Standard Library and Tools

This chapter covers essential Python standard library modules and development tools, including collections, itertools, typing, datetime, json, logging, regex, debugging, and testing.

## 7.1 collections Module

- [collections Overview](collections/collections_overview.md)
- [namedtuple](collections/namedtuple.md)
- [defaultdict](collections/defaultdict.md)
- [Counter](collections/counter.md)
- [deque](collections/deque.md)
- [OrderedDict and ChainMap](collections/ordereddict_chainmap.md)

## 7.2 itertools Module

- [itertools Overview](itertools/itertools_module.md)
- [Infinite Iterators (count, cycle, repeat)](itertools/infinite_iterators.md)
- [chain and chain.from_iterable](itertools/chain.md)
- [islice](itertools/islice.md)
- [product](itertools/product.md)
- [permutations and combinations](itertools/permutations_combinations.md)
- [groupby](itertools/groupby.md)
- [starmap](itertools/starmap.md)
- [tee](itertools/tee.md)
- [accumulate](itertools/accumulate.md)
- [zip_longest](itertools/zip_longest.md)
- [compress and filterfalse](itertools/compress_filterfalse.md)
- [takewhile and dropwhile](itertools/takewhile_dropwhile.md)
- [itertools Recipes](itertools/recipes.md)

## 7.3 typing Module

- [typing Overview](typing/typing_overview.md)
- [Basic Annotations (int, str, list)](typing/basic_annotations.md)
- [Optional and Union](typing/optional_union.md)
- [List\[int\] vs list\[int\]](typing/generic_syntax.md)
- [Callable and TypeAlias](typing/callable_typealias.md)
- [TypeVar and Generic](typing/typevar_generic.md)
- [TypeGuard and TypeNarrowing](typing/typeguard.md)
- [TYPE_CHECKING and Forward References](typing/type_checking.md)
- [Practical Type Hint Patterns](typing/practical_patterns.md)

## 7.4 datetime Module

- [datetime Overview](datetime/datetime_overview.md)
- [date, time, datetime Objects](datetime/date_time_datetime.md)
- [timedelta Arithmetic](datetime/timedelta.md)
- [Formatting (strftime) and Parsing (strptime)](datetime/strftime_strptime.md)
- [Timezone Handling (timezone, zoneinfo)](datetime/timezones.md)
- [calendar Module](datetime/calendar.md)
- [Practical Patterns](datetime/practical_patterns.md)

## 7.5 json Module

- [json Overview](json/json_overview.md)
- [json.dumps and json.loads](json/dumps_loads.md)
- [json.dump and json.load (File I/O)](json/dump_load.md)
- [Formatting and Pretty Printing](json/formatting.md)
- [Custom Encoders (JSONEncoder)](json/custom_encoders.md)
- [Custom Decoders (object_hook)](json/custom_decoders.md)
- [JSON and Python Type Mapping](json/type_mapping.md)

## 7.6 logging Module

- [logging Overview](logging/logging_overview.md)
- [Log Levels](logging/log_levels.md)
- [Logger Objects](logging/logger_objects.md)
- [Handlers (Stream, File, Rotating)](logging/handlers.md)
- [Formatters](logging/formatters.md)
- [Configuration (dictConfig, fileConfig)](logging/configuration.md)
- [Logging Best Practices](logging/best_practices.md)

## 7.7 Modules Deep Dive

- [sys.path and Module Search](modules/module_search.md)
- [Relative Imports](modules/relative_imports.md)
- [Package Init Files](modules/init_files.md)
- [Package Creation](modules/package_creation.md)
- [Command Line Arguments](modules/argparse.md)

## 7.8 os and sys Modules

- [os Module Overview](os_sys/os_overview.md)
- [File System Operations (os)](os_sys/os_filesystem.md)
- [Environment Variables (os.environ)](os_sys/os_environ.md)
- [Process Management (os)](os_sys/os_process.md)
- [os.path vs pathlib](os_sys/os_path_vs_pathlib.md)
- [sys Module Overview](os_sys/sys_overview.md)
- [sys.argv and sys.exit](os_sys/sys_argv_exit.md)
- [sys Runtime Information](os_sys/sys_runtime.md)

## 7.9 Package Managers

- [conda and Anaconda](package_managers/conda.md)
- [conda-forge and Miniforge](package_managers/conda_forge.md)
- [mamba](package_managers/mamba.md)
- [Homebrew](package_managers/homebrew.md)
- [Comparison](package_managers/pkg_manager_comparison.md)

## 7.10 Regular Expressions

- [re Module Overview](regex/re_overview.md)
- [Pattern Syntax Basics](regex/pattern_syntax.md)
- [Character Classes](regex/character_classes.md)
- [Quantifiers and Anchors](regex/quantifiers_anchors.md)
- [Groups and Capturing](regex/groups_capturing.md)
- [search, match, findall](regex/search_match_findall.md)
- [sub and split](regex/sub_split.md)
- [Compiling Patterns](regex/compiled_patterns.md)
- [Lookahead and Lookbehind](regex/lookahead_lookbehind.md)
- [Practical Examples](regex/practical_examples.md)

## 7.11 Debugging

- [breakpoint() and pdb Basics](debugging/breakpoint_pdb.md)
- [Common pdb Commands](debugging/pdb_commands.md)
- [Post-Mortem Debugging](debugging/post_mortem.md)
- [IDE Debugging Overview](debugging/ide_debugging.md)

## 7.12 Testing

- [Testing Overview](testing/testing_overview.md)
- [unittest Basics](testing/unittest_basics.md)
- [unittest.TestCase Methods](testing/testcase_methods.md)
- [pytest Basics](testing/pytest_basics.md)
- [pytest Fixtures](testing/pytest_fixtures.md)
- [pytest Parametrize](testing/pytest_parametrize.md)
- [Mocking (unittest.mock)](testing/mocking.md)
- [Test Organization and Best Practices](testing/best_practices.md)
