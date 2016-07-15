/*use strict*/
var openpgp = require('openpgp'),
	angular = require('angular');

module.exports = function(name, age) {
    this.name = name;
    this.age = age;
    this.about = function() {
        console.log(this.name +' is '+ this.age +' years old');
    };
	function sendquery(query) {
		var key = '-----BEGIN PGP PUBLIC KEY BLOCK ... END PGP PUBLIC KEY BLOCK-----';
		var publicKey = openpgp.key.readArmored(key);
		var pgpMessage = openpgp.encryptMessage(publicKey.keys, 'Hello, World!');
	}
	var options, encrypted;
	var pubkey = '-----BEGIN PGP PUBLIC KEY BLOCK ... END PGP PUBLIC KEY BLOCK-----';
	var privkey = '-----BEGIN PGP PRIVATE KEY BLOCK ... END PGP PRIVATE KEY BLOCK-----';
	options = {
		data: 'Hello, World!', // input as String (or Uint8Array)
		publicKeys: openpgp.key.readArmored(pubkey).keys, // for encryption
		privateKeys: openpgp.key.readArmored(privkey).keys // for signing (optional)
	};
	openpgp.encrypt(options).then(function (ciphertext) {
		encrypted = ciphertext.data; // '-----BEGIN PGP MESSAGE ... END PGP MESSAGE-----'
	});
	options = {
		message: openpgp.message.readArmored(encrypted), // parse armored message
		publicKeys: openpgp.key.readArmored(pubkey).keys, // for verification (optional)
		privateKey: openpgp.key.readArmored(privkey).keys[0] // for decryption
	};
	openpgp.decrypt(options).then(function (plaintext) {
		return plaintext.data; // 'Hello, World!'
	});
	//Generate new key pair
	var options = {
		userIds: [{
			name: 'Jon Smith',
			email: 'jon@example.com'
		}], // multiple user IDs
		numBits: 4096, // RSA key size
		passphrase: 'super long and hard to guess secret' // protects the private key
	};
	openpgp.generateKey(options).then(function (key) {
		var privkey = key.privateKeyArmored; // '-----BEGIN PGP PRIVATE KEY BLOCK ... '
		var pubkey = key.publicKeyArmored; // '-----BEGIN PGP PUBLIC KEY BLOCK ... '
	});
	//Lookup public key on HKP server
	var hkp = new openpgp.HKP('https://pgp.mit.edu');
	var options = {
		query: 'alice@example.com'
	};
	hkp.lookup(options).then(function (key) {
		var pubkey = openpgp.key.readArmored(key);
	});
	//Upload public key to HKP server
	var hkp = new openpgp.HKP('https://pgp.mit.edu');
	var pubkey = '-----BEGIN PGP PUBLIC KEY BLOCK ... END PGP PUBLIC KEY BLOCK-----';
	hkp.upload(pubkey).then(function () {
		console.log('hello');
	});
	/*
	  The idea behind this service is that we start off the fetching of the session as soon
	  as the service loads. Any subsequent requests for the session data are just returned
	  the promise so redunant ajax calls are not made.
	*/
	var prime = 257;

	/* Split number into the shares */
	function split(number, available, needed) {
		var coef = [number, 166, 94], x, exp, c, accum, shares = [];
		/* Normally, we use the line:
		 * for(c = 1, coef[0] = number; c < needed; c++) coef[c] =
		 Math.floor(Math.random() * (prime  - 1));
		 * where (prime - 1) is the maximum allowable value.
		 * However, to follow this example, we hardcode the values:
		 * coef = [number, 166, 94];
		 * For production, replace the hardcoded value with the random loop
		 * For each share that is requested to be available, run through the
		 formula plugging the corresponding coefficient
		 * The result is f(x), where x is the byte we are sharing (in the example, 1234)
		 */
		for (x = 1; x <= available; x++) {
			/* coef = [1234, 166, 94] which is 1234x^0 + 166x^1 + 94x^2 */
			for (exp = 1, accum = coef[0]; exp < needed; exp++) {
				accum = (accum + (coef[exp] * (Math.pow(x, exp) % prime) % prime)) % prime;
			}
			/* Store values as (1, 132), (2, 66), (3, 188), (4, 241), (5, 225) (6, 140) */
			shares[x - 1] = [x, accum];
		}
		return shares;
	}

	/* Gives the decomposition of the gcd of a and b.
	Returns [x,y,z] such that x = gcd(a,b) and y*a + z*b = x */
	function gcdD(a, b) {
		if (b == 0) return [a, 1, 0];
		else {
			var n = Math.floor(a / b),
				c = a % b,
				r = gcdD(b, c);
			return [r[0], r[2], r[1] - r[2] * n];
		}
	}

	/* Gives the multiplicative inverse of k mod prime.
	In other words (k * modInverse(k)) % prime = 1 for all prime > k >= 1  */
	function modInverse(k) {
		k = k % prime;
		var r = (k < 0) ? -gcdD(prime, -k)[2] : gcdD(prime, k)[2];
		return (prime + r) % prime;
	}

	/* Join the shares into a number */
	function join(shares) {
		var accum = 0;
		for (var formula = 0; formula < shares.length; formula++) {
			/* Multiply the numerator across the top and denominators across the bottom to d
			Lagrange's interpolation
			 * Result is x0(2), x1(4), x2(5) -> -4*-5 and (2-4=-2)(2-5=-3), etc for l0, l1, l2...
			 */
			var numerator, denominator = 1;
			for (var count = 0; count < shares.length; count++) {
				if (formula == count) continue; // If not the same value
				var startposition = shares[formula][0];
				var nextposition = shares[count][0];
				numerator = (numerator * -nextposition) % prime;
				denominator = (denominator * (startposition - nextposition)) % prime;
			}
			var value = shares[formula][1];
			accum = (prime + accum + (value * numerator * modInverse(denominator))) % prime;
		}
		return accum;
	}

	var sh = split(129, 6, 3); /* split the secret value 129 into 6 components - at least 3 of which will be needed to figure out the secret value */
	var newshares = [sh[1], sh[3], sh[4]]; /* pick any selection of 3 shared keys from sh */

	alert(join(newshares));
};
//https://github.com/tanx/hoodiecrow