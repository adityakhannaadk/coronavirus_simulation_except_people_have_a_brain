# coronavirus_simulation_except_people_have_a_brain
Coronavirus simulation except people actually have a brain.

Most simulations involve people randomly moving or a basic algorithm that decides their movement in correspondence to those around them. My model takes a different approach. I used a basic neural network for each "mover" on the simulation field to decide their next movement. I needed it to be basic to prevent computational complexity. This is still just a concept in its embryonic stage. I don't have a great amount of knowledge in epidemiology (though I find it interesting) this is just an idea I had. 

I did try to make it as efficient in terms of computational complexity as possible. There are 3 main ways I did this:
* Use a 5,2 neural hidden layer configuration
* Use the same neural network for each mover (hive mind)
* Retrain the model on new data from one randomly picked mover
* Only get the response radius and use an algorithm pick apart x and y movements

However, remember that for 1000 movers, even a very basic MLP will still run slowly. 

# Credits
The simulation graphic was written by someone else. I will link it when I find it again
