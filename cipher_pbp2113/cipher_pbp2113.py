def cipher(text, shift, encrypt=True):
 	"""
	Encrypts strings by converting each element of a string to a new character by shifting a uniform length along the alphabetical scale.

	Parameters
	----------
	  text : str
	    A Python string.
	  shift : int
	    The number of digits you want to shift each element of text by along the alphabetical scale.
	  encrypt : boolean
	    Indicates the direction with which text should be shifted by string. True is rightward, False is leftward. Default=True.

	Returns
	-------
	str
	  The encrypted string.

	Examples
	--------
	>>> cipher_pbp2113.cipher("Johnny", 2)
	'LqjppA'
	Equivalently:
	>>> cipher_pbp2113.cipher("LqjppA", -2)
	'Johnny'
	>>> cipher_pbp2113.cipher("LqjppA", 2, encrypt=False)
	'Johnny'
 	"""

 	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
 	new_text = ''
 	for c in text:
 		index = alphabet.find(c)
 		if index == -1:
 			new_text += c
 		else:
 			new_index = index + shift if encrypt == True else index - shift
 			new_index %= len(alphabet)
 			new_text += alphabet[new_index:new_index+1]
 	return new_text