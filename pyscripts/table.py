def parse_csv_lines(lines, splitter=","):
    num_columns = len(lines[0].split(splitter))
    table = []
    for line in lines:
        cells = [x.strip() for x in line.split(splitter)]
        assert(len(cells) == num_columns)
        table += [cells]
    return table

def get_maxlen_of_row(table):
    num_columns = len(table[0])
    max_cell_lens = [0] * num_columns
    for line in table:
        assert(len(line) == num_columns)
        max_cell_lens = [max(x[0], x[1]) for x in zip(max_cell_lens, [len(t) for t in line])]
    return max_cell_lens

def get_table_string(table, table_line="-", padding=" ", line_splitter="+", cell_splitter="|"):
    max_cell_lens = get_maxlen_of_row(table)
    divideline = line_splitter + line_splitter.join([table_line * (t + 2 * len(padding)) for t in max_cell_lens]) + line_splitter + "\n"
    result = divideline
    row_index = 0
    for line in table:
        result_line = [padding + cell + padding * (newlen - len(cell) + 1) for (cell, newlen) in zip(line, max_cell_lens)]
        result += cell_splitter + (cell_splitter.join(result_line)) + cell_splitter + "\n"
        if row_index == 0:
            result += divideline
        row_index += 1
    result += divideline
    return result