import re


_DEFINITION_TYPES = {
  'def': 'function',
  'class': 'class',
  'method': 'method',
}

_SYMBOL_REGEX = re.compile(r'( )*(def|class) ([\w_]+)')


def _get_last_class_name(symbol_list):
  '''Get last class name defined in the symbol list.

  Args:
    symbol_list: List of parsed symbols.

  Returns:
    String name of last class defined or None.
  '''
  for symbol_name, symbol_type, _ in reversed(symbol_list):
    if symbol_type == _DEFINITION_TYPES['class']:
      return symbol_name
  return None

def parse_code(code):
  '''Parses class and function names from given string.

  Args:
    code: String containing python code to be parsed.

  Returns:
    List of tuples containing definition name and definition type and source
    class for methods e.g. ('my_func', 'function', None).
  '''
  results = []
  for symbol in re.finditer(_SYMBOL_REGEX, code):
    if symbol.group(1):
      results.append((
          symbol.group(3),
          _DEFINITION_TYPES['method'],
          _get_last_class_name(results)))
    else:
      results.append((
          symbol.group(3),
          _DEFINITION_TYPES.get(symbol.group(2)),
          None))
  return results
