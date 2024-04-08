project(
  'tree-sitter-grammars',
  'c', 'cpp',
  default_options : [
    'cpp_eh=none',
    'c_link_args=-z,relro,-z,now',
    'cpp_link_args=-z,relro,-z,now',
    'warning_level=0',
  ]
)

fs = import('fs')

grammars = fs.read('paths.txt').strip().split('\n')

foreach grammar : grammars
  grammar = grammar.split()
  name = grammar[0]
  source = grammar[1]

  source_files = [source / 'src/parser.c']

  if fs.is_file(source / 'src/scanner.cc')
    source_files += source / 'src/scanner.cc'
  elif fs.is_file(source / 'src/scanner.c')
    source_files += source / 'src/scanner.c'
  endif

  library(
    name,
    source_files,
    include_directories : source / 'src',
    install : true,
    install_dir : get_option('libdir') / 'helix/runtime/grammars',
    name_prefix : '',
  )

endforeach
