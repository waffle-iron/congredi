class ppq():
	def __init__(self):
		kr = pgpy.PGPKeyring(glob.glob(os.path.expanduser('~/.gnupg/*ring.gpg')))
		kr = pgpy.PGPKeyring()
		loaded = kr.load(glob.glob(os.path.expanduser('~/.gnupg/*ring.gpg')))
		key.protect("C0rrectPassphr@se", SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)
		with enc_key.unlock("C0rrectPassphr@se"):
			pass
	def genkey(comment=None):
		key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
		uid = pgpy.PGPUID.new('Nikola Tesla')  # comment and email are optional
		key.add_uid(uid, usage={KeyFlags.Sign}, hashes=[HashAlgorithm.SHA512, HashAlgorithm.SHA256],
					ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.Camellia256],
					compression=[CompressionAlgorithm.BZ2, CompressionAlgorithm.Uncompressed],
					key_expires=timedelta(days=365))
		subkey = pgpy.PGPKey.new(PubKeyAlgorithm.RSA, 4096)
		key.add_subkey(subkey, usage={KeyFlags.Authentication})
		empty_key = pgpy.PGPKey()
		empty_key.parse(keyblob)
		key, _ = pgpy.PGPKey.from_file('path/to/key.asc')
		key, _ = pgpy.PGPKey.from_blob(keyblob)
		key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
		uid = pgpy.PGPUID.new('Abraham Lincoln', comment='Honest Abe', email='abraham.lincoln@whitehouse.gov')
		key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
					hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
					ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
					compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed])
		return genkey
	def certifykey(keyid):
		someones_pubkey |= mykey.certify(someones_pubkey)
		cert = mykey.certify(someones_pubkey.userids[0], level=SignatureType.Persona_Cert)
		someones_pubkey.userids[0] |= cert
		for uid in someones_pubkey.userids:
			uid |= mykey.certify(uid)
		return signedkey
	def armouritem(keyid=None,message=None):
		#keybytes = key.__bytes__()
		keybytes = bytes(key)
		keystr = str(key)
		msgbytes = bytes(message)
		msgstr = str(message)
		msgbytes = message.__bytes__()
	def genmessage(keyid,message):
		_message = pgpy.PGPMessage.new("This is a brand spankin' new message!")
		file_message = pgpy.PGPMessage.new("path/to/a/file", file=True)
		ct_message = pgpy.PGPMessage.new("This is a shiny new cleartext document. Hooray!",
										 cleartext=True)
		message_from_file = pgpy.PGPMessage.from_file("path/to/a/message")
		message_from_blob = pgpy.PGPMessage.from_blob(msg_blob)
		encrypted_message = rsa_pub.encrypt(message)
		cipher = pgpy.constants.SymmetricKeyAlgorithm.AES256
		sessionkey = cipher.gen_key()
		enc_msg = pubkey1.encrypt(message, cipher=cipher, sessionkey=sessionkey)
		enc_msg = pubkey2.encrypt(enc_msg, cipher=cipher, sessionkey=sessionkey)
		del sessionkey
		enc_message = message.encrypt("S00per_Sekr3t")
		dec_message = enc_message.decrypt("S00per_Sekr3t")
		pgpstr = str(pgpobj)
		pgpbytes = bytes(pgpobj)
		pgpbytes = pgpobj.__bytes__()
	def signmessage(keyid,message):
		sig = sec.sign("I have just signed this text!")
		message |= sec.sign(message)
		timesig = sec.sign(None)
		lone_sig = sec.sign(None, notation={"cheese status": "standing alone"})
	def verifymessage(message):
		pub.verify("I have just signed this text!", sig)
		pub.verify(message)
		for uid in someones_pubkey.userids:
			pub.verify(uid)
		pub.verify(someones_pubkey)


class Crypto():
	#openpgp = OpenPGP.worker
	#https://pythonhosted.org/PGPy/examples.html
	def __init__(self):
		pass
	def initialize(method):
		return(self.method)
	# stv - shufflesum
	# openpgp
	# secret sharing
