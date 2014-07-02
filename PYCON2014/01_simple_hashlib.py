# import hashlib

# def checkio(hashed_string, algorithm):
#     try:
#         return hashlib.new(algorithm, hashed_string.encode("utf8")).hexdigest()
#     except ValueError:
#         return hashlib.sha512(hashed_string.encode("utf8")).hexdigest()



checkio = lambda u, e: getattr(__import__('hashlib'), e)(u.encode("utf8")).hexdigest()

