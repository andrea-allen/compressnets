# compressnets

To use `compressnets`, install the package via the PyPi (or TestPyPi) index via
`pip install -i https://test.pypi.org/simple/ compressnets`.

## Most basic usage
The core elements of `compressnets` are the objects, `network.TemporalNetwork` and `network.Snapshot`,
and the algorithm `compression.Compressor.compress(...)`.

As an example, create a NumPy array to represent your adjacency matrices:
```
snapshot_1 = [[0, 0, 1],
            [0, 0, 1],
            [1, 1, 0]]
snapshot_2 = [[0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]]
snapshot_3 = [[0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]]
```
Then create a list of `Snapshot` objects from your arrays, equipped with a consecutive start and end time for each:
```
infect_rate = 0.5
snapshots = [network.Snapshot(start_time=0, end_time=1, beta=infect_rate, A=snapshot_1),
             network.Snapshot(start_time=1, end_time=2, beta=infect_rate, A=snapshot_2),
             network.Snapshot(start_time=2, end_time=3, beta=infect_rate, A=snapshot_3)]
```
Then create a `TemporalNetwork` object to contain all of your ordered snapshots:
```
your_temporal_network = network.TemporalNetwork(snapshots)
```
Using the algorithmic compression from our paper [link], you can compress
the temporal network into a desired number of compressed snapshots (in this example, 5), by calling on an instance of the static `Compressor` class
```
your_compressed_network_result = compression.Compressor.compress(your_temporal_network,
                                                          compress_to=5,
                                                          how='optimal')
``` 
which will return the new `TemporalNetwork` object, and also the total induced error from the snapshots that
were selected for compression. The elements can be accessed via a dictionary as
```
your_compressed_network = your_compressed_network_result["compressed_network"]
total_induced_error = your_compressed_network_result["error"]
```
To compress your original network into an even division and aggregation of snapshots,
not using our algorithm, you can call `compress` and changing the `how` argument to `even`:
```
your_even_compressed_network_result = compression.Compressor.compress(your_temporal_network,
                                                          compress_to=5,
                                                          how='even')
even_compressed_network = your_even_compressed_network_result["compressed_network"]                                                    
``` 

From the resulting compressed `TemporalNetwork` objects, you can now access your snapshots as you
would with your original temporal network, by accessing the `snapshots` member via
```
your_new_snapshots = your_compressed_network.snapshots
```
from which you can access each snapshot's new duration, adjacency matrix, start and end times.
