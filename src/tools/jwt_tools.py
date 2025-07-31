
from dataclasses import dataclass
import jwt

@dataclass
class JWTTools:
    secret_key: str
    algorithm: str = 'HS256'
    
    
    def decode_token(self, token: str) -> dict:
        return jwt.decode(
            token,
            key=self.secret_key,
            algorithms=[self.algorithm]
        )
        
    def generate_token(self, payload: dict) -> str:
        return jwt.encode(
            payload=payload,
            key=self.secret_key,
            algorithm=self.algorithm
        )
