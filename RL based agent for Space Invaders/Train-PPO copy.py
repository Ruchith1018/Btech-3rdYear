from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
N = 100000000
if rank == 0:
  s = sum(range(N/2))
  comm.send(s,dest=2,tag=11)
elif rank == 1:
  s = sum(range(N/2+1,N))
  comm.send(s,dest=2,tag=11)
elif rank == 2:
  s1 = comm.recv(source=0, tag=11)
  s2 = comm.recv(source=1, tag=11)
print (s1+s2)