# Overview


# Public Key

## Vetting users (certify/revoke keys)

The public key of the user, stored within the database, gets updated by
a valid certification of that user by someone else.

## Account Management (public key or fernet symetric)

Recovering account details involves using the private key on client-side
JS, without it, the account shouldn't be recoverable.

## Jurisdiction Administration (Threshold keys)

Unlocking jurisdiction options requires consent from all the parties
sharing a common secret (technically blockchain threshold sigs, not
Secure Secret Sharing, unless I can find an uncompromising method).

## Voting and elections (Shuffle-Sum)

Elections contain both a publicly signed poll ranking, and a private
shuffle-sum operation. The poll is attached to the user's profile,
while the Shuffle-Sum operation is used to verify their actual private vote.