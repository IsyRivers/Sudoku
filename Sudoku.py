from math import *

class Sudoku:
	
	def start(self, tempBoard = ""):
		if(tempBoard == ""):
			self.__getBoard();
		else:
			self.__processBoard(tempBoard);
			self.__solve();

	def __processBoard(self, tempBoard):
		self.size = sqrt(sqrt(len(tempBoard)));
		if self.size != 3:
			quit();
		self.size = int(self.size);
		self.__createBoard(tempBoard);
		
	def __printBoard(self):
		print("\n");
		for i in range(0, self.size**2):
			if(i%3 == 0):
				print("\n"+self.size**2*("------"));
			else:
				print();
			for j in range(0,self.size**2):
				if(j != 0 and j%3 == 0):
					print("||", end = "" );
				else:
					print(" | ", end = "" );#seperator
				if(self.board[i][j] == 0):
					print("   ", end = "" );#cell value
				else:
					print(str(self.board[i][j]).center(3), end = "" );#cell value
			
	def __createBoard(self, tempboard):
		self.board = [[0 for row in range(self.size**2)] for col in range(self.size**2)]
		count = 0;
		for row in range(0, self.size**2):
			for col in range(0,self.size**2):
				tempboard[count];
				self.board[row][col] = int(tempboard[count]);
				count += 1;
		
	def __check(self, row, col, value):
		if(not (self.__checkCol(col, value) or self.__checkRow(row, value) or self.__checkCell(row, col,value))):
			return True;
		else:
			return False;
		
	def __checkCol(self, col, value):
		for row in range(0, self.size**2):
			if(self.board[row][col] == value):
				return True;
		return False;
			
	def __checkRow(self, row, value):
		for col in range(0, self.size**2):
			if(self.board[row][col] == value):
				return True;
		return False;
		
	def __checkCell(self, row, col, value):
		rowOffset = row//self.size;
		colOffset = col//self.size;

		for r in range(0, self.size):
			for c in range(0, self.size):
				if(self.board[r+rowOffset*self.size][c+colOffset*self.size] == value):
					return True;
		return False;
	

	def __solve(self):
		self.__solveLogic();
		if(self.__hasEmpties()):
			temp = self.__getEmpty();
			self.__solveRecursive(temp[0], temp[1]);

		self.__printBoard();
		
	def __isSolved(self):
		for row in range(0, self.size**2):
				for col in range(0, self.size**2):
					if(self.board[row][col] == 0):
						return False;
		return True;

	def __hasEmpties(self):
		return not self.__isSolved();

	def __getEmpty(self):
		cell = [];
		for row in range(0, self.size**2):
			for col in range(0, self.size**2):
				if(self.board[row][col] == 0):
					cell.append(row);
					cell.append(col);
					return cell;
		cell.append(-1);
		cell.append(-1);
		return cell;
		
	def __solveLogic(self):
		changeMade = True;
		while(changeMade and self.__hasEmpties()):
			changeMade = False;
			for row in range(0, self.size**2):
				for col in range(0, self.size**2):
					if(self.board[row][col] == 0):
						possible = self.__listPossibilities(row, col);
						if(len(possible) == 1):
							self.board[row][col] = possible.pop();
							changeMade = True;

	def __solveRecursive(self, row, col):	
		possibilities = self.__listPossibilities(row, col);
			
		while(len(possibilities) > 0):
			self.board[row][col] = possibilities.pop();
			if(self.__hasEmpties()):
				temp = self.__getEmpty();
				if(self.__solveRecursive(temp[0], temp[1])):
					return True;
				else:
					self.board[row][col] = 0;
			else:
				return True;

	def __listPossibilities(self, row, col): #needs tweaking
		possibilities = [];
		if(self.board[row][col] > 0):
			possibilities.append(self.board[row][col]);
			return possibilities;
		for checkVal in range(1, self.size**2+1):
			if (self.__check(row, col, checkVal)):
				possibilities.append(checkVal);
		return possibilities;              

	def __promptFile(self):
		print("Prompting for file");
		input();

	def __getBoardFromFile(self):
		print("Getting Board ")

	def __readFile(self):
		print(board)
		
	def __writeBoard2File(self):
		print(board)    

	def testFunctions(self):
		possible = self.__listPossibilities(5, 3);
		print(str(possible));
