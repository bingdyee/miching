"""
pymmh3 was written by Fredrik Kihlander and enhanced by Swapnil Gusani, and is placed in the public
domain. The authors hereby disclaim copyright to this source code.
"""


def hash(key, seed = 0x0):
    key = bytearray( key.encode() )

    def fmix( h ):
        h ^= h >> 16
        h  = ( h * 0x85ebca6b ) & 0xFFFFFFFF
        h ^= h >> 13
        h  = ( h * 0xc2b2ae35 ) & 0xFFFFFFFF
        h ^= h >> 16
        return h

    length = len( key )
    nblocks = int( length / 4 )

    h1 = seed

    c1 = 0xcc9e2d51
    c2 = 0x1b873593

    # body
    for block_start in range( 0, nblocks * 4, 4 ):
        # ??? big endian?
        k1 = key[ block_start + 3 ] << 24 | \
             key[ block_start + 2 ] << 16 | \
             key[ block_start + 1 ] <<  8 | \
             key[ block_start + 0 ]
             
        k1 = ( c1 * k1 ) & 0xFFFFFFFF
        k1 = ( k1 << 15 | k1 >> 17 ) & 0xFFFFFFFF # inlined ROTL32
        k1 = ( c2 * k1 ) & 0xFFFFFFFF
        
        h1 ^= k1
        h1  = ( h1 << 13 | h1 >> 19 ) & 0xFFFFFFFF # inlined ROTL32
        h1  = ( h1 * 5 + 0xe6546b64 ) & 0xFFFFFFFF

    # tail
    tail_index = nblocks * 4
    k1 = 0
    tail_size = length & 3

    if tail_size >= 3:
        k1 ^= key[ tail_index + 2 ] << 16
    if tail_size >= 2:
        k1 ^= key[ tail_index + 1 ] << 8
    if tail_size >= 1:
        k1 ^= key[ tail_index + 0 ]
    
    if tail_size > 0:
        k1  = ( k1 * c1 ) & 0xFFFFFFFF
        k1  = ( k1 << 15 | k1 >> 17 ) & 0xFFFFFFFF # inlined ROTL32
        k1  = ( k1 * c2 ) & 0xFFFFFFFF
        h1 ^= k1

    #finalization
    unsigned_val = fmix( h1 ^ length )
    if unsigned_val & 0x80000000 == 0:
        return unsigned_val
    else:
        return -( (unsigned_val ^ 0xFFFFFFFF) + 1 )


def hash128(key, seed = 0x0):
    ''' Implements 128bit murmur3 hash. '''

    key = bytearray(key.encode())

    def fmix(k):
            k ^= k >> 33
            k  = ( k * 0xff51afd7ed558ccd ) & 0xFFFFFFFFFFFFFFFF
            k ^= k >> 33
            k  = ( k * 0xc4ceb9fe1a85ec53 ) & 0xFFFFFFFFFFFFFFFF
            k ^= k >> 33
            return k

    length = len(key)
    nblocks = int(length / 16)

    h1 = seed
    h2 = seed

    c1 = 0x87c37b91114253d5
    c2 = 0x4cf5ad432745937f

    #body
    for block_start in range( 0, nblocks * 8, 8 ):
        # ??? big endian?
        k1 = key[ 2 * block_start + 7 ] << 56 | \
                key[ 2 * block_start + 6 ] << 48 | \
                key[ 2 * block_start + 5 ] << 40 | \
                key[ 2 * block_start + 4 ] << 32 | \
                key[ 2 * block_start + 3 ] << 24 | \
                key[ 2 * block_start + 2 ] << 16 | \
                key[ 2 * block_start + 1 ] <<  8 | \
                key[ 2 * block_start + 0 ]

        k2 = key[ 2 * block_start + 15 ] << 56 | \
                key[ 2 * block_start + 14 ] << 48 | \
                key[ 2 * block_start + 13 ] << 40 | \
                key[ 2 * block_start + 12 ] << 32 | \
                key[ 2 * block_start + 11 ] << 24 | \
                key[ 2 * block_start + 10 ] << 16 | \
                key[ 2 * block_start + 9 ] <<  8 | \
                key[ 2 * block_start + 8 ]

        k1  = ( c1 * k1 ) & 0xFFFFFFFFFFFFFFFF
        k1  = ( k1 << 31 | k1 >> 33 ) & 0xFFFFFFFFFFFFFFFF # inlined ROTL64
        k1  = ( c2 * k1 ) & 0xFFFFFFFFFFFFFFFF
        h1 ^= k1

        h1 = ( h1 << 27 | h1 >> 37 ) & 0xFFFFFFFFFFFFFFFF # inlined ROTL64
        h1 = ( h1 + h2 ) & 0xFFFFFFFFFFFFFFFF
        h1 = ( h1 * 5 + 0x52dce729 ) & 0xFFFFFFFFFFFFFFFF

        k2  = ( c2 * k2 ) & 0xFFFFFFFFFFFFFFFF
        k2  = ( k2 << 33 | k2 >> 31 ) & 0xFFFFFFFFFFFFFFFF # inlined ROTL64
        k2  = ( c1 * k2 ) & 0xFFFFFFFFFFFFFFFF
        h2 ^= k2

        h2 = ( h2 << 31 | h2 >> 33 ) & 0xFFFFFFFFFFFFFFFF # inlined ROTL64
        h2 = ( h1 + h2 ) & 0xFFFFFFFFFFFFFFFF
        h2 = ( h2 * 5 + 0x38495ab5 ) & 0xFFFFFFFFFFFFFFFF

    #tail
    tail_index = nblocks * 16
    k1 = 0
    k2 = 0
    tail_size = length & 15

    if tail_size >= 15:
        k2 ^= key[ tail_index + 14 ] << 48
    if tail_size >= 14:
        k2 ^= key[ tail_index + 13 ] << 40
    if tail_size >= 13:
        k2 ^= key[ tail_index + 12 ] << 32
    if tail_size >= 12:
        k2 ^= key[ tail_index + 11 ] << 24
    if tail_size >= 11:
        k2 ^= key[ tail_index + 10 ] << 16
    if tail_size >= 10:
        k2 ^= key[ tail_index +  9 ] << 8
    if tail_size >=  9:
        k2 ^= key[ tail_index +  8 ]

    if tail_size > 8:
        k2  = ( k2 * c2 ) & 0xFFFFFFFFFFFFFFFF
        k2  = ( k2 << 33 | k2 >> 31 ) & 0xFFFFFFFFFFFFFFFF # inlined ROTL64
        k2  = ( k2 * c1 ) & 0xFFFFFFFFFFFFFFFF
        h2 ^= k2

    if tail_size >=  8:
        k1 ^= key[ tail_index +  7 ] << 56
    if tail_size >=  7:
        k1 ^= key[ tail_index +  6 ] << 48
    if tail_size >=  6:
        k1 ^= key[ tail_index +  5 ] << 40
    if tail_size >=  5:
        k1 ^= key[ tail_index +  4 ] << 32
    if tail_size >=  4:
        k1 ^= key[ tail_index +  3 ] << 24
    if tail_size >=  3:
        k1 ^= key[ tail_index +  2 ] << 16
    if tail_size >=  2:
        k1 ^= key[ tail_index +  1 ] << 8
    if tail_size >=  1:
        k1 ^= key[ tail_index +  0 ]

    if tail_size > 0:
        k1  = ( k1 * c1 ) & 0xFFFFFFFFFFFFFFFF
        k1  = ( k1 << 31 | k1 >> 33 ) & 0xFFFFFFFFFFFFFFFF # inlined ROTL64
        k1  = ( k1 * c2 ) & 0xFFFFFFFFFFFFFFFF
        h1 ^= k1

    #finalization
    h1 ^= length
    h2 ^= length

    h1  = ( h1 + h2 ) & 0xFFFFFFFFFFFFFFFF
    h2  = ( h1 + h2 ) & 0xFFFFFFFFFFFFFFFF

    h1  = fmix( h1 )
    h2  = fmix( h2 )

    h1  = ( h1 + h2 ) & 0xFFFFFFFFFFFFFFFF
    h2  = ( h1 + h2 ) & 0xFFFFFFFFFFFFFFFF

    return ( h2 << 64 | h1 )


def hash64(key, seed = 0x0):
    ''' Implements 64bit murmur3 hash. Returns a tuple. '''

    hash_128 = hash128(key, seed)

    unsigned_val1 = hash_128 & 0xFFFFFFFFFFFFFFFF
    if unsigned_val1 & 0x8000000000000000 == 0:
        signed_val1 = unsigned_val1
    else:
        signed_val1 = -( (unsigned_val1 ^ 0xFFFFFFFFFFFFFFFF) + 1 )

    unsigned_val2 = ( hash_128 >> 64 ) & 0xFFFFFFFFFFFFFFFF
    if unsigned_val2 & 0x8000000000000000 == 0:
        signed_val2 = unsigned_val2
    else:
        signed_val2 = -( (unsigned_val2 ^ 0xFFFFFFFFFFFFFFFF) + 1 )

    return ( int( signed_val1 ), int( signed_val2 ) )


def hash_bytes( key, seed = 0x0 ):
    ''' Implements 128bit murmur3 hash. Returns a byte string. '''

    hash_128 = hash128( key, seed)

    bytestring = ''

    for _ in range(0, 16, 1):
        lsbyte = hash_128 & 0xFF
        bytestring = bytestring + str( chr( lsbyte ) )
        hash_128 = hash_128 >> 8

    return bytestring
