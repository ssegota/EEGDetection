import numpy
import winsound
from scipy.signal import butter, lfilter, freqz

class MyOVBox(OVBox):        
	def __init__(self):
		OVBox.__init__(self)
		self.signalHeader = None
	
	def process(self):
                value=0
		for chunkIndex in range( len(self.input[0]) ):
			if(type(self.input[0][chunkIndex]) == OVSignalHeader):
				self.signalHeader = self.input[0].pop()
				
				outputHeader = OVSignalHeader(
				self.signalHeader.startTime, 
				self.signalHeader.endTime, 
				[1, self.signalHeader.dimensionSizes[1]], 
				['Mean']+self.signalHeader.dimensionSizes[1]*[''],
				self.signalHeader.samplingRate)
				
				self.output[0].append(outputHeader)
				
			elif(type(self.input[0][chunkIndex]) == OVSignalBuffer):
				chunk = self.input[0].pop()
				numpyBuffer = numpy.array(chunk).reshape(tuple(self.signalHeader.dimensionSizes))
				numpyBuffer = numpyBuffer.mean(axis=0)
				chunk = OVSignalBuffer(chunk.startTime, chunk.endTime, numpyBuffer.tolist())
				self.output[0].append(chunk)
                                value+=1		
			elif(type(self.input[0][chunkIndex]) == OVSignalEnd):
				self.output[0].append(self.input[0].pop())	 			





                        #threshold for signal activation
			#Experimentally determined might need adjustements
			thresh=7
			##Low-Pass Filter implementation
			fs=30
			cutoff=20.0
			order=6
			nyq = 0.5 * fs
			normal_cutoff = cutoff / nyq
			b, a = butter(order, normal_cutoff, btype='low', analog=False)
			y = lfilter(b, a, numpyBuffer)

			#y = numpy.fabs(y)
			#High Pass Filter Implementation
			cutoff2=4.0
			normal_cutoff = cutoff2 / nyq
			b, a = butter(order, normal_cutoff, btype='high', analog=False)
			y = lfilter(b, a, y)
			
			freq=int(numpy.fabs(int(numpy.floor(y.sum()))))
			print(freq)
			###
			if(freq>thresh):
					winsound.Beep(200, 100)


box = MyOVBox()
