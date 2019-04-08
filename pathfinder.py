from PIL import image, ImageDraw

class Map:

	def __init__(self, filename):
		with open(filename) as file:
			self.elevations = [[int(e) for e in line.split()] for line in filename
			self.max_elevation = max([max(row) for row in self.elevations])
            self.min_elevation = min([min(row) for row in self.elevations])

	def elevation_coordinates(self, x, y):
		return self.elevations[y][x]

	def shade_scale(self, x, y):
		return int(self.elevation_coordinates(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255)


	def draw_map(self):
		self.picture = Image.new('RBGA', (len(self.elevations[0], len(self.elevations)))
		self.generate = ImageDraw.Draw(self.picture)
			for x in range(len(self.elevations[0])):
				for y in range(len(self.elevations)):
		self.picture.putpixel((x, y),x self.shade_scale(x, y), self.shade_scale(x, y), self.shade_scale(x, y))
		self.picture.save('map.png')

if __name__ == '__main__':
	elevation_map = Map('elevation_small.txt')
	elevation_map.draw_map()
