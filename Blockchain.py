'''
blockchain 클래스는 체인을 관리하는 역할을 한다.
블록체인 클래스에는 거래와 체인에 새로운 블록을 추가하는 기능들이 있다.
'''
class Blockchain(object) :
    def __init__(self):
        self.chain = []
        self.current_transctions=[]

        # 새로운 제네시스 블록 만들기
        self.new_block(previous_hash=1, proof=100)
    
    def new_block(self, proof, previous_hash=None):
        '''
        블록체인에 들어갈 새로운 블록을 만드는 코드이다.
        index는 블록의 번호, timestamp 는 블록이 만들어진 시간이다.
        transaction은 블록에 포함될 거래이다.
        
        '''
        pass

    @staticmethod
    def hash(block):
        # 블록의 해시값을 출력한다.
        pass
    
    @property
    def last_block(self):
        # 체인의 가장 블록을 반환한다.
        pass

    def new_transaction(self,sender,recipient,amount):
        """
        새로운 거래는 다음으로 채굴될 블록에 포함되게 된다. 거래는 3개의 인자로 구성되어 있다.
        sender와 recipient는 string으로 각각 수신자와 송신자의 주소이다.
        amount는 int로 전송되는 양을 의미한다.
        return 은 해당 거래가 속해질 블록의 숫자를 의미한다.
        """
        self.current_transctions.append({
            'sender': sender,
            'recipient': recipient,
            'amount' : amount
        })
        
        return self.last_block['index'] + 1



'''
블록은 어떻게 생겼는가?
각 블록은 인덱스, 타임스탬프, 거래내역, 증명, 이전 블록의 해쉬를 가지고 있다.

previous_hash 위 코드가 블록체인에 변경 불가능성을 넣어주기 때문이다.

블록에 거래 ㅐ더하기
new_transaction()이 이를 위해 필요하다.

new_transaction()가 리스트에 거래를 추가 하고 나면, 거래가 추가될 블록의 인덱스를 반환한다.
새로운 블록 만들기

우리 blockchain이 인스턴스화 되었을때, 반드시 geneis block이 필요하다. 이전블록이 없는 최초의블록.
또한 genesis block에 proof를 추가해야 한다.

'''
