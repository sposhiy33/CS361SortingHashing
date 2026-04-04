"""
    Heavily inspired by the FNV hash function created by Glenn Fowler, Landon Curt Noll, and Kiem-Phong Vo
"""
import math

class bloom_filter:
    def __init__(self, hash_file, acceptable_error_rate):
        """
        Initialize the Bloom filter with a built-in Python bit array.
        """
        file_size = num_lines(hash_file)
        self.size = get_optimal_size(file_size, acceptable_error_rate)
        self.hash_count = get_optimal_hash_count(self.size, file_size) 
        # Adding 7 here to effectively "ceiling" when doing integer division
        num_bytes = (self.size + 7) // 8
        self.byte_array = bytearray(num_bytes)
        print(f"Hashing...")
        self.load(hash_file)
        print("-" * 30)
        
    def fnv1a_hash(self, item, seed):
        """
        A custom implementation of the 32-bit FNV-1a hash algorithm.
        """
        # Standard 32-bit FNV-1a parameters
        fnv_prime = 0x01000193       # 16777619
        offset_basis = 0x811c9dc5    # 2166136261
        
        # We append the 'seed' to the item so each of our k passes 
        # generates a completely different hash result.
        seeded_item = f"{seed}:{item}"
        
        hash_value = offset_basis
        
        # Process the string byte by byte
        for byte in seeded_item.encode('utf-8'):
            hash_value = hash_value ^ byte                    # XOR the byte into the bottom of the hash
            hash_value = (hash_value * fnv_prime) % (2**32)   # Multiply by prime and constrain to 32 bits
            
        return hash_value

    def get_hash_indices(self, item):
        """
        Generate 'k' distinct bit indices with a double hash
        Standard double hash formula:
            g_i(x) = (h_1(x) + i * h_2(x)) % m
        """
        # Generate two base hashes using different seeds
        h1 = self.fnv1a_hash(item, seed="A")
        h2 = self.fnv1a_hash(item, seed="B")
        
        indices = []
        for i in range(self.hash_count):
            # The linear combination creates a new index for each i
            index = (h1 + i * h2) % self.size
            indices.append(index)
            
        return indices

    def add(self, item):
        """
        Hash the item and set the corresponding bits to 1.
        """
        for index in self.get_hash_indices(item):
            # Find which byte the bit lives in
            byte_index = index // 8
            # Find which bit within that byte to flip
            bit_offset = index % 8
            # Use a bitmask (1 shifted by offset) to set the bit to 1
            self.byte_array[byte_index] |= (1 << bit_offset)

    def check(self, item):
        """
        Hash the item and check if all corresponding bits are 1.
        """
        for index in self.get_hash_indices(item):
            byte_index = index // 8
            bit_offset = index % 8
            # Check if the specific bit is 0 using bitwise AND
            if not (self.byte_array[byte_index] & (1 << bit_offset)):
                # Return false if confident bit doesn't exist
                return False
                
        return True # Probably in the set
    
    def load(self, file_path):
        """
        Load given file into hash
        """
        try:
            with file_path.open('r', encoding='utf-8') as infile:
                
                for file_size, line in enumerate(infile):
                    self.add(line.strip())
                    
            print(f"Success! {file_size + 1} lines have been hashed.")
        
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
                
        return True # Probably in the set
    
def num_lines(file_path):
    num_lines = 0
    try:
        with file_path.open('r', encoding='utf-8') as infile:
            
            for line in enumerate(infile):
                num_lines = num_lines + 1
                
            print(f"{num_lines} lines have been counted.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return num_lines
    
def get_optimal_size(n, p):
    """
    Calculate the optimal bit array size (m).
    :param n: Expected number of items.
    :param p: Acceptable false positive probability (e.g., 0.01).
    :return: Integer size of the bit array.
    """
    m = -(n * math.log(p)) / (math.log(2) ** 2)
    print(f"Optimal bit array size: {m}")
    return int(math.ceil(m))

def get_optimal_hash_count(m, n):
    """
    Calculate the optimal number of hash functions (k).
    :param m: Size of the bit array.
    :param n: Expected number of items.
    :return: Integer number of hash functions.
    """
    k = (m / n) * math.log(2)
    print(f"Optimal hash count: {k}")
    return int(math.ceil(k))



    