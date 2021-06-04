import random
# độ lớn quần thể
POPULATION_SIZE = 2000

# tỉ lệ số lượng cá thể làm bố mẹ trong quần thể
MATING_POOL_SIZE = 0.5

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.-;:_!"'#%&/()=?@${[]}'''

TARGET = "Bach Khoa Ho Chi Minh University"

class Individual(object):
    def __init__(self, chromosome):
        assert len(chromosome) == len(TARGET)
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    # lấy một gene ngẫu nhiên trong tập gene cho trước (GENES)
    @classmethod
    def get_random_gene(self):
        return random.choice(GENES)

    # ngẫu nhiên tạo ra một nhiễm sắc thể mới
    @classmethod
    def create_gnome(self):
        chromosome_length = len(TARGET)
        return [c for c in random.choices(GENES, k = chromosome_length)]

    # toán tử giao chéo
    def crossover(self, partner):
        p = random.randint(0, len(TARGET))
        c1 = self.chromosome[:p] + partner.chromosome[p:]
        c2 = partner.chromosome[:p] + self.chromosome[p:]
        return [c1, c2]

    # cho cá thể hiện tại giao phối với partner
    def mate(self, partner):
        childs = self.crossover(partner)

        # đột biến hai cá thể con
        for child in childs:
            for i in range(len(child)):
                # mỗi gene có tỉ lệ 10% bị đột biến
                if random.random() < 0.1:
                    child[i] = Individual.get_random_gene()

        return [Individual(childs[0]), Individual(childs[1])]

    # hàm tính độ tốt (thể trạng) của cá thể
    # cụ thể ở đây là số lượng phần tử năm đúng vị trí
    # với chuỗi kết quả của chúng ta
    def calculate_fitness(self):
        diff = 0
        for i in range(len(TARGET)):
            if self.chromosome[i] != TARGET[i]:
                diff += 1
        return diff

    # hàm phụ trợ cho việc in trong print
    def __repr__(self):
        return "{} - fitness: {}".format(''.join(c for c in self.chromosome), self.fitness)

    # hàm so sánh nhỏ hơn (<) để có thể sắp xếp dễ dàng
    def __lt__(self, o):
        return self.fitness < o.fitness

def main():
    population = []
    generation = 1

    elitism_rate = 0.1

    # khởi tạo quần thể
    for i in range(POPULATION_SIZE):
        chromosome = Individual.create_gnome()
        population.append(Individual(chromosome))

    # khi chưa tìm được thì ta vẫn tiếp tục lặp
    while True:
        best_individual = population[0]
        for individual in population:
            if best_individual < individual:
                best_individual = individual

        print('Generation {} - Best individual: {}'.format(generation, population[0]))
        
        # nếu cá thể tốt nhất trong quần thể có thể trạng bằng 0 (đồng nghĩa với chuỗi là
        # "Bach Khoa Ho Chi Minh University") thì dừng vòng lặp
        if population[0].fitness == 0:
            break

        # lấy 10% cá thể tốt nhất để thực hiện mô hình cá thể ưu tú
        population = sorted(population)
        elitism = int(elitism_rate * POPULATION_SIZE)
        next_generation = population[:elitism]

        # chọn tập những cá thể làm bố mẹ
        mating_pool = population[:int(MATING_POOL_SIZE * POPULATION_SIZE)]

        # khi số lượng cá thể trong quần thể mới còn ít hơn số lượng cá thể được xác định ban đầu
        while len(next_generation) < POPULATION_SIZE:
            # chọn 2 cá thể để làm bố và mẹ ngẫu nhiên từ tập được xác định lúc trước
            parent1 = random.choice(mating_pool)
            parent2 = random.choice(mating_pool)

            childs = parent1.mate(parent2)

            # thêm 2 cá thể con mới được sinh ra vào quần thể mới
            next_generation.extend(childs)

        # gán đúng số lượng cá thể trong quần thể mới được sinh ra làm quần thể hiện tại
        population = next_generation[:POPULATION_SIZE]
        generation += 1

    print('\nAnswer foun at generation {} with population size {}\nIndividual: {}'.format(generation, POPULATION_SIZE, population[0]))

if __name__ == '__main__':
    main()
