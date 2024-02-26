from Simulation import *
import itertools

sim = Simulation()

lane_space = 3.5
intersection_size = 12
length = 100

# SOUTH, EAST, NORTH, WEST

# Intersection in
sim.create_segment((lane_space / 2, length + intersection_size / 2), (lane_space / 2, intersection_size / 2))
sim.create_segment((length + intersection_size / 2, -lane_space / 2), (intersection_size / 2, -lane_space / 2))
sim.create_segment((-lane_space / 2, -length - intersection_size / 2), (-lane_space / 2, -intersection_size / 2))
sim.create_segment((-length - intersection_size / 2, lane_space / 2), (-intersection_size / 2, lane_space / 2))
# Intersection out
sim.create_segment((-lane_space / 2, intersection_size / 2), (-lane_space / 2, length + intersection_size / 2))
sim.create_segment((intersection_size / 2, lane_space / 2), (length + intersection_size / 2, lane_space / 2))
sim.create_segment((lane_space / 2, -intersection_size / 2), (lane_space / 2, -length - intersection_size / 2))
sim.create_segment((-intersection_size / 2, -lane_space / 2), (-length - intersection_size / 2, -lane_space / 2))
# Straight
sim.create_segment((lane_space / 2, intersection_size / 2), (lane_space / 2, -intersection_size / 2))
sim.create_segment((intersection_size / 2, -lane_space / 2), (-intersection_size / 2, -lane_space / 2))
sim.create_segment((-lane_space / 2, -intersection_size / 2), (-lane_space / 2, intersection_size / 2))
sim.create_segment((-intersection_size / 2, lane_space / 2), (intersection_size / 2, lane_space / 2))
# Right turn
sim.create_quadratic_bezier_curve((lane_space / 2, intersection_size / 2), (lane_space / 2, lane_space / 2),
                                  (intersection_size / 2, lane_space / 2))
sim.create_quadratic_bezier_curve((intersection_size / 2, -lane_space / 2), (lane_space / 2, -lane_space / 2),
                                  (lane_space / 2, -intersection_size / 2))
sim.create_quadratic_bezier_curve((-lane_space / 2, -intersection_size / 2), (-lane_space / 2, -lane_space / 2),
                                  (-intersection_size / 2, -lane_space / 2))
sim.create_quadratic_bezier_curve((-intersection_size / 2, lane_space / 2), (-lane_space / 2, lane_space / 2),
                                  (-lane_space / 2, intersection_size / 2))
# Left turn
sim.create_quadratic_bezier_curve((lane_space / 2, intersection_size / 2), (lane_space / 2, -lane_space / 2),
                                  (-intersection_size / 2, -lane_space / 2))
sim.create_quadratic_bezier_curve((intersection_size / 2, -lane_space / 2), (-lane_space / 2, -lane_space / 2),
                                  (-lane_space / 2, intersection_size / 2))
sim.create_quadratic_bezier_curve((-lane_space / 2, -intersection_size / 2), (-lane_space / 2, lane_space / 2),
                                  (intersection_size / 2, lane_space / 2))
sim.create_quadratic_bezier_curve((-intersection_size / 2, lane_space / 2), (lane_space / 2, lane_space / 2),
                                  (lane_space / 2, -intersection_size / 2))
sim.create_traffic_signal((0,0))


def getAnimation(start, goal):
    turnAnimation = [
        [[0, 5], 12],
        [[1, 6], 13],
        [[2, 7], 14],
        [[3, 4], 15],
        [[0, 7], 15],
        [[1, 4], 12],
        [[2, 5], 13],
        [[3, 6], 14]
    ]

    if (goal - start) % 2 != 0:
        for i in turnAnimation:
            if i[0] == [start, goal]:
                return int(i[1])
    else:
        return goal + 2





vehicles = []
for i, j in list(itertools.permutations([0, 1, 2, 3], 2)):
    j += 4
    vehicles.append((1, {'path': [i, getAnimation(i, j), j]}))
vg = VehicleGenerator({
    'vehicle_rate': 30,
    'vehicles': [
        # straight forward
        (1, {'path': [0, 8, 6], 'v': 16.6, 'a': 10}),
        (1, {'path': [1, 9, 7], 'v': 16.6, 'a': 10}),
        (1, {'path': [2, 10, 4], 'v': 16.6, 'a': 10}),
        (1, {'path': [3, 11, 5], 'v': 16.6, 'a': 10}),

        # right turn
        (1, {'path': [0, 12, 5], 'v': 16.6, 'a': 10}),
        (1, {'path': [1, 13, 6], 'v': 16.6, 'a': 10}),
        (1, {'path': [2, 14, 7], 'v': 16.6, 'a': 10}),
        (1, {'path': [3, 15, 4], 'v': 16.6, 'a': 10}),

        # left turn
        (1, {'path': [0, 16, 7], 'v': 16.6, 'a': 10}),
        (1, {'path': [1, 17, 4], 'v': 16.6, 'a': 10}),
        (1, {'path': [2, 18, 5], 'v': 16.6, 'a': 10}),
        (1, {'path': [3, 19, 6], 'v': 16.6, 'a': 10})

    ]
})

sim.add_vehicle_generator(vg)

# v = Vehicle({'path': [0], 'x': 20, 'v':16.6})
# sim.add_vehicle(v)

# v = Vehicle({'path': [0]})
# sim.add_vehicle(v)

win = Window(sim)
win.run()
win.show()
