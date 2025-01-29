'''
==================================================
File: main.py
Project: simopty
File Created: Sunday, 8th December 2024
Author: Edoardo Cabiati (edoardo.cabiati@mail.polimi.it)
Under the supervision of: Politecnico di Milano
==================================================
'''


"""
The main.py module contains the main function of the program.
"""

import os
import graph as dg
from graph import model_to_graph
import domain as dm
import mapper as mp
import simulator_stub as ss
from dirs import *
import optimizers as op
from utils.plotting_utils import *
from utils.ga_utils import *
from utils.partitioner_utils import *
from utils.ani_utils import *
import tensorflow.keras as keras
import tensorflow.keras.layers as layers
from tensorflow.keras.utils import plot_model
import nocsim

def test_model(input_shape):
    
    inputs = layers.Input(shape=input_shape)
    x = layers.Conv2D(3, kernel_size=(3, 3), activation='linear') (inputs)
    x = layers.MaxPooling2D(pool_size=(2, 2))(x)
    x = layers.Conv2D(6, kernel_size=(3, 3))(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.MaxPooling2D(pool_size=(2, 2))(x)
    x = layers.Flatten()(x)
    x = layers.Dense(64)(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    x = layers.Dense(24, activation='relu')(x)
    x = layers.Dense(10, activation='softmax')(x)
    model = keras.Model(inputs=inputs, outputs=x)
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    summary = model.summary()
    return model


def load_model(model_name):
    available_models = ["ResNet50", "MobileNetV2", "MobileNet", "ResNet18"]
    if model_name not in available_models:
        raise ValueError(f"Model not available. Please choose from the following: {', '.join(available_models)}")
    
    # Load the model
    model = keras.applications.__getattribute__(model_name)(weights='imagenet')
    return model

if __name__ == "__main__":
    
    # # Create a TaskGraph object
    # dep_graph = dg.TaskGraph()

    # # Define the structure of the dependency graph
    # dep_graph.add_task_fully_qualified(id=3, type = "COMP_OP", layer_id = 0, size= 10, weight_size = 5, ct_required=40, dep = [0])
    # dep_graph.add_task_fully_qualified(id=4, type = "COMP_OP", layer_id = 0, size = 10,weight_size = 5, ct_required=30, dep = [1])
    # dep_graph.add_task_fully_qualified(id=5, type = "COMP_OP", layer_id = 0, size = 10, weight_size = 5, ct_required=20, dep = [2])
    # dep_graph.add_dependency_fully_qualified("start", 3, id = 0, type = "WRITE", size = 8, pt_required= 8, cl = 0, dep= [-1])
    # dep_graph.add_dependency_fully_qualified("start", 4, id = 1, type = "WRITE", size = 6, pt_required= 6, cl = 0, dep= [-1])
    # dep_graph.add_dependency_fully_qualified("start", 5, id = 2, type = "WRITE", size = 4, pt_required= 4, cl = 0, dep= [-1])
    # dep_graph.add_task_fully_qualified(id = 11, type = "COMP_OP", layer_id = 1, size = 10, weight_size = 5, ct_required = 10, dep = [6, 7, 9])
    # dep_graph.add_task_fully_qualified(id = 12, type = "COMP_OP", layer_id = 1, size = 10, weight_size = 5,ct_required = 10, dep = [8, 10])
    # dep_graph.add_dependency_fully_qualified(3, 11, id = 6, type = "WRITE_REQ",  size = 4, pt_required = 4, cl = 0, dep = [3])
    # dep_graph.add_dependency_fully_qualified(4, 11, id = 7, type = "WRITE_REQ",  size = 1, pt_required = 1, cl = 0, dep = [4])
    # dep_graph.add_dependency_fully_qualified(5, 11, id = 9, type = "WRITE_REQ",  size = 1, pt_required = 1, cl = 0, dep = [5])
    # dep_graph.add_dependency_fully_qualified(3, 12, id = 8, type = "WRITE_REQ",  size = 2, pt_required = 2, cl = 0, dep = [3])
    # dep_graph.add_dependency_fully_qualified(5, 12, id = 10, type = "WRITE_REQ",  size = 1, pt_required = 1, cl = 0, dep = [5])
    # dep_graph.add_task_fully_qualified(id = 15, type = "COMP_OP", layer_id = 2, size = 10, weight_size = 5,ct_required = 10, dep = [13, 14])
    # dep_graph.add_dependency_fully_qualified(11, 15, id = 13, type = "WRITE_REQ",  size = 1, pt_required = 1, cl = 0, dep = [11])
    # dep_graph.add_dependency_fully_qualified(12, 15, id = 14, type = "WRITE_REQ",  size = 1, pt_required = 1, cl = 0, dep = [12])
    # dep_graph.add_dependency_fully_qualified(15, "end", id = 16, type = "WRITE",  size = 1, pt_required = 1, cl = 0, dep = [15])
    # plot_graph(dep_graph)
    # # Create a Grid object
    # grid = dm.Grid()
    # grid.init(3, 2, dm.Topology.TORUS)

    # # Create a Mapper object
    # mapper = mp.Mapper()
    # mapper.init(dep_graph, grid)


    # # Ant's job: decide the mapping
    # mapping = {3 : 0, 4 : 1, 5 : 2, 11 : 3, 12 : 4, 15 : 7}
    # # mapping = {3 : 0, 4 : 1, 5 : 2, 11 : 6, 12 : 4, 15 : 7}
    # # mapping = {3 : 0, 4 : 3, 5 : 2, 11 : 6, 12 : 4, 15 : 7}
    # # mapping = {3 : 3, 4 : 3, 5 : 2, 11 : 6, 12 : 4, 15 : 7}


    # mapper.set_mapping(mapping)
    # plot_mapping_gif(mapper)
    # # Create the configuration file from the arch and the structure
    # mapper.mapping_to_json(CONFIG_DUMP_DIR + "/dump1.json", file_to_append=ARCH_FILE)
    
    # Define a Optimization object

    # params = op.ACOParameters(
    #     n_ants = 20,
    #     rho = 0.05,
    #     n_best = 10,
    #     n_iterations = 150,
    #     alpha = 1.,
    #     beta = 1.2,
    # )

    # opt = op.AntColony(params, grid, dep_graph)

    # shortest = opt.run(once_every=1, show_traces= True)
    # print(shortest[0])
    # print(opt.path_length(shortest[0], verbose = True))


    # params = op.GAParameters(
    #     sol_per_pop = 40,
    #     n_parents_mating=30,
    #     n_generations = 100,
    #     mutation_probability = .5,
    #     crossover_probability = .9,
    # )

    # opt = op.GeneticAlgorithm(params, grid, dep_graph)

    # shortest = opt.run()

    # opt.ga_instance.plot_fitness()
    # print(shortest[0], 1/shortest[1])

    # model = test_model((28, 28, 1))
    # # # model = load_model("ResNet50")
    # # # model = load_model("MobileNet")
    # # # model = load_model("MobileNetV2")

    # #model.summary()
    # #plot_model(model, to_file="visual/model.png", show_shapes=True)
    # # # analyze_ops(model, True)

    # # # print(split_spatial_dims(model.layers[2], 2))
    
    # task_graph = model_to_graph(model, verbose=True)
    # plot_graph(task_graph)

    # grid = dm.Grid()
    # grid.init(6, 2, dm.Topology.TORUS)

    # params = op.ACOParameters(
    #     n_ants = 100,
    #     rho = 0.05,
    #     n_best = 20,
    #     n_iterations = 150,
    #     alpha = 1.,
    #     beta = 1.2,
    # )
    # n_procs = 4 #what is the biggest number of processors that can be used regarding the grid size?
    # # opt = op.ParallelAntColony(n_procs, params, grid, dep_graph) !deph_graph is the old one (test)
    # opt = op.ParallelAntColony(n_procs, params, grid, task_graph)

    # shortest = opt.run(once_every=1, show_traces= False)
    # print(shortest[1])
    # print(opt.path_length(shortest[1], verbose = True))
    
    # # Load the statistics and plot the results
    # stats = np.load("visual/statistics.npy", allow_pickle=True).item()
    # #print(stats)

    # Create a SimulatorStub object
    stub = ss.SimulatorStub(EX_DIR)

    # Run the simulation
    processors = list(range(6))
    #config_files = [os.path.join(RUN_FILES_DIR, f) for f in os.listdir(RUN_FILES_DIR) if f.endswith('.json')]
    #results, logger = stub.run_simulations_in_parallel(config_files=config_files, processors=processors, verbose=True)
    #results, logger = stub.run_simulation("config_files/dumps/dump.json", verbose = True)
    #test
    results, logger = stub.run_simulation("config_files/runs/test_run.json", verbose = True)
    print(results)
    #print(logger.print_events())
    # print(logger.events[1].info.history[0].rsource)
    # print(logger.events[1].info.history[0].rsink)
    # print(logger.events[1].info.history[0].start)
    # print(logger.events[1].info.history[0].end)
    # print(logger.events[1].info.history[1].rsource)
    # print(logger.events[1].info.history[1].rsink)
    # print(logger.events[1].info.history[1].start)
    # print(logger.events[1].info.history[1].end)
    # print(logger.events[1].info)

    #NoCPlotter().plot(logger,"config_files/runs/test_run.json" )
    
    #Initialize plotter with timeline support
    plotter = NoCTimelinePlotter()
    plotter.plot(logger, "config_files/runs/test_run.json")  # Original 3D plot

    # Generate 2D timeline
    plotter.setup_timeline(logger)
    plotter.plot_timeline()
    plotter._print_node_events()

    # Save/display both plots
    plt.savefig("visual/timeline.png")  # Static 2D timeline
    #plt.show()                   # Show 3D animation + 2D timeline
        
    # print(logger[0].events[3].info.history)
    # print(logger[0].events[3].info.history[0])
    # print(logger[0].events[3].info.history[1])
    # print(logger[0].events[3].info.history[2])
    print("\n")
    for event in logger.events:
        print(event)
        print(f"Event ID: {event.id}, Type: {event.type}, Cycle: {event.cycle}, Additional info: {event.additional_info}," 
              f"Info: {event.info}")
        if event.type == nocsim.EventType.START_COMPUTATION:
            print(f"Node ID: {event.info.node}")
        elif event.type == nocsim.EventType.OUT_TRAFFIC:
            print(f"History: {event.info.history}")
    print("-------------------")
    # info_0 = logger.get_event_info(0)
    # info_1 = logger.get_event_info(1)
    # info_2 = logger.get_event_info(2)
    # print(info_0)
    # print(info_1)
    # print(info_2)
    # print("-------------------")



