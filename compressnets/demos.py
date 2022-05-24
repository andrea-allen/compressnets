from compressnets.compression import *
import gzip
import json


class Sample:

    @staticmethod
    def get_sample_temporal_network():
        with gzip.open('sample_network', 'r') as fin:  # 4. gzip
            json_bytes = fin.read()  # 3. bytes (i.e. UTF-8)

        json_str = json_bytes.decode('utf-8')  # 2. string (i.e. JSON)
        loaded_network = TemporalNetworkDecoder().decode(json_str=json_str)
        return loaded_network
