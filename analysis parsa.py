class BarChart(BaseChart):
    def init(self, categories, values):
        self.categories = categories
        self.values = values
        plt.figure(figsize=(8, 5))
        
    def plot(self, color='skyblue'):
        plt.bar(self.categories, self.values, color=color)
        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title('Bar Chart Example')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

# مثال استفاده:
# chart = BarChart(['A', 'B', 'C', 'D'], [15, 30, 45, 20])
# chart.plot(color='orange')
# chart.show()