# Given a string representing a matrix of
# numbers, return the rows and columns of that
# matrix.

class Matrix:
    def __init__(self, matrix_string):
        """
        Convert the matrix_string in a list of rows of ints
        
        :param matrix_string: str - a string representing a matrix
        """
        self.rows = []
        for string in matrix_string.split("\n"):
            row = string.split()
            row_of_ints = []
            for char in row:
                row_of_ints.append(int(char))
            self.rows.append(row_of_ints)

    def row(self, index):
        """
        Get a specified row from a list of rows
        
        :return: [int] - the row of ints
        """
        return self.rows[index-1]

    def column(self, index):
        """
        Get a specified column from the row-indexed elements
        
        :return: [int] - a list of row-indexed elements
        """
        columns = []
        for row in self.rows:
            columns.append(row[index-1])
        return columns
