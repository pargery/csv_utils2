
class IndentMessages:
    def __init__(self):
        self.space_char = ' '
        self.space_per_indent = 2

        # width of space in which to print the SUM (%d)
        self.number_width = 4

        # desired total width of [spaces][message][sum] line written to a report
        self.total_width = 40

    def indent_message(self, level, msg, sum):

        num_spaces = level * self.space_per_indent
        while num_spaces > self.total_width:
            num_spaces = (level - 1) * self.space_per_indent

        msg_width  = self.total_width - num_spaces


        format_str='{{0:s}}{{1:{0:d}s}}{{2:-{1:d}d}}'.format(msg_width,self.number_width)
        #print 'DEBUG: Using format string {0:s}'.format(format_str)

        spaces = self.space_char * num_spaces
        indented_msg = format_str.format(spaces, msg, sum)

        return indented_msg


if __name__ == '__main__':
    print "Testing IndentMessages.indent_messages()"

    test = IndentMessages()
    for level in range(1,5):
        msg = 'Thing {0:d}:'.format(level)
        sum = level * 10
        print test.indent_message(level, msg, sum)

