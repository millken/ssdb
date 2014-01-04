# encoding=utf-8
# Generated by cpy
# 2014-01-04 23:10:30.210288
import os, sys
from sys import stdin, stdout

import socket
class SSDB_Response(object):
	pass


	def __init__(this, code='', data_or_message=None):
		pass
		this.code = code
		this.data = None
		this.message = None

		if code=='ok':
			pass
			this.data = data_or_message
		else:
			pass
			this.message = data_or_message

	def __repr__(this):
		pass
		return ((((str(this.code) + ' ') + str(this.message)) + ' ') + str(this.data))

	def ok(this):
		pass
		return this.code=='ok'

	def not_found(this):
		pass
		return this.code=='not_found'

class SSDB(object):
	pass


	def __init__(this, host, port):
		pass
		this.recv_buf = ''
		this._closed = False
		this.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		this.sock.connect(tuple([host, port]))
		this.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

	def close(this):
		pass

		if not (this._closed):
			pass
			this.sock.close()
			this._closed = True

	def closed(this):
		pass
		return this._closed

	def request(this, cmd, params=None):
		pass

		if params==None:
			pass
			params = []
		params = ([cmd] + params)
		this.send(params)
		resp = this.recv()

		if resp==None:
			pass
			return SSDB_Response('error', 'Unknown error')

		if len(resp)==0:
			pass
			return SSDB_Response('disconnected', 'Connection closed')

		# {{{ switch: cmd
		_continue_1 = False
		while True:
			if False or ((cmd) == 'set') or ((cmd) == 'zset') or ((cmd) == 'hset') or ((cmd) == 'qpush') or ((cmd) == 'del') or ((cmd) == 'zdel') or ((cmd) == 'hdel') or ((cmd) == 'multi_set') or ((cmd) == 'multi_del') or ((cmd) == 'multi_hset') or ((cmd) == 'multi_hdel') or ((cmd) == 'multi_zset') or ((cmd) == 'multi_zdel'):
				pass

				if len(resp)>1:
					pass
					return SSDB_Response(resp[0], int(resp[1]))
				else:
					pass
					return SSDB_Response(resp[0], 1)
				break
			if False or ((cmd) == 'get') or ((cmd) == 'hget') or ((cmd) == 'qfront') or ((cmd) == 'qback') or ((cmd) == 'qpop'):
				pass

				if resp[0]=='ok':
					pass

					if len(resp)==2:
						pass
						return SSDB_Response('ok', resp[1])
					else:
						pass
						return SSDB_Response('server_error', 'Invalid response')
				else:
					pass
					return SSDB_Response(resp[0])
				break
			if False or ((cmd) == 'incr') or ((cmd) == 'decr') or ((cmd) == 'zincr') or ((cmd) == 'zdecr') or ((cmd) == 'hincr') or ((cmd) == 'hdecr') or ((cmd) == 'hsize') or ((cmd) == 'zsize') or ((cmd) == 'qsize') or ((cmd) == 'zget') or ((cmd) == 'zrank') or ((cmd) == 'zrrank') or ((cmd) == 'hclear') or ((cmd) == 'zclear') or ((cmd) == 'qclear'):
				pass

				if resp[0]=='ok':
					pass

					if len(resp)==2:
						pass
						try:
							pass
							val = int(resp[1])
							return SSDB_Response('ok', val)
						except Exception , e:
							pass
							return SSDB_Response('server_error', 'Invalid response')
					else:
						pass
						return SSDB_Response('server_error', 'Invalid response')
				else:
					pass
					return SSDB_Response(resp[0])
				break
			if False or ((cmd) == 'keys') or ((cmd) == 'zkeys') or ((cmd) == 'hkeys') or ((cmd) == 'hlist') or ((cmd) == 'zlist'):
				pass
				data = []

				if resp[0]=='ok':
					pass
					i = 1

					while i<len(resp):
						pass
						data.append(resp[i])
						pass
						i += 1
				return SSDB_Response(resp[0], data)
				break
			if False or ((cmd) == 'scan') or ((cmd) == 'rscan') or ((cmd) == 'hscan') or ((cmd) == 'hrscan'):
				pass

				if resp[0]=='ok':
					pass

					if len(resp) % 2==1:
						pass
						data = {'index': [],'items': {},}
						i = 1

						while i<len(resp):
							pass
							k = resp[i]
							v = resp[(i + 1)]
							data['index'].append(k)
							data['items'][k] = v
							pass
							i += 2
						return SSDB_Response('ok', data)
					else:
						pass
						return SSDB_Response('server_error', 'Invalid response')
				else:
					pass
					return SSDB_Response(resp[0])
				break
			if False or ((cmd) == 'zscan') or ((cmd) == 'zrscan') or ((cmd) == 'zrange') or ((cmd) == 'zrrange'):
				pass

				if resp[0]=='ok':
					pass

					if len(resp) % 2==1:
						pass
						data = {'index': [],'items': {},}
						i = 1

						while i<len(resp):
							pass
							k = resp[i]
							v = resp[(i + 1)]
							try:
								pass
								v = int(v)
							except Exception , e:
								pass
								v = - (1)
							data['index'].append(k)
							data['items'][k] = v
							pass
							i += 2
						return SSDB_Response('ok', data)
					else:
						pass
						return SSDB_Response('server_error', 'Invalid response')
				else:
					pass
					return SSDB_Response(resp[0])
				break
			if False or ((cmd) == 'exists') or ((cmd) == 'hexists') or ((cmd) == 'zexists'):
				pass
				data = False

				if resp[0]=='ok':
					pass

					if len(resp)>=2:
						pass

						if resp[1]=='1':
							pass
							data = True
				return SSDB_Response(resp[0], data)
				break
			if False or ((cmd) == 'multi_exists') or ((cmd) == 'multi_hexists') or ((cmd) == 'multi_zexists'):
				pass
				data = {}

				if len(resp) % 2==1:
					pass
					i = 1

					while i<len(resp):
						pass
						k = resp[i]

						if resp[(i + 1)]=='1':
							pass
							v = True
						else:
							pass
							v = False
						data[k] = v
						pass
						i += 2
				return SSDB_Response('ok', data)
				break
			if False or ((cmd) == 'multi_get') or ((cmd) == 'multi_hget'):
				pass

				if resp[0]=='ok':
					pass

					if len(resp) % 2==1:
						pass
						data = {}
						i = 1

						while i<len(resp):
							pass
							k = resp[i]
							v = resp[(i + 1)]
							data[k] = v
							pass
							i += 2
						return SSDB_Response('ok', data)
					else:
						pass
						return SSDB_Response('server_error', 'Invalid response')
				else:
					pass
					return SSDB_Response(resp[0])
				break
			if False or ((cmd) == 'multi_hsize') or ((cmd) == 'multi_zsize') or ((cmd) == 'multi_zget'):
				pass

				if resp[0]=='ok':
					pass

					if len(resp) % 2==1:
						pass
						data = {}
						i = 1

						while i<len(resp):
							pass
							k = resp[i]
							v = int(resp[(i + 1)])
							data[k] = v
							pass
							i += 2
						return SSDB_Response('ok', data)
					else:
						pass
						return SSDB_Response('server_error', 'Invalid response')
				else:
					pass
					return SSDB_Response(resp[0])
				break
			### default

			if len(resp)>1:
				pass
				data = []
				i = 1

				while i<len(resp):
					pass
					data.append(resp[i])
					pass
					i += 1
			else:
				pass
				data = ''
			return SSDB_Response(resp[0], data)
			break
			break
			if _continue_1:
				continue
		# }}} switch

		return SSDB_Response('error', 'Unknown error')

	def send(this, data):
		pass
		ps = []

		_cpy_r_0 = _cpy_l_1 = data
		if type(_cpy_r_0).__name__ == 'dict': _cpy_b_3=True; _cpy_l_1=_cpy_r_0.iterkeys()
		else: _cpy_b_3=False;
		for _cpy_k_2 in _cpy_l_1:
			if _cpy_b_3: p=_cpy_r_0[_cpy_k_2]
			else: p=_cpy_k_2
			pass
			p = str(p)
			ps.append(str(len(p)))
			ps.append(p)
		nl = '\n'
		s = (nl.join(ps) + '\n\n')
		try:
			pass

			while True:
				pass
				ret = this.sock.send(s)

				if ret==0:
					pass
					return - (1)
				s = s[ret : ]

				if len(s)==0:
					pass
					break
		except socket.error , e:
			pass
			return - (1)
		return ret

	def net_read(this):
		pass
		try:
			pass
			data = this.sock.recv(1024 * 8)
		except Exception , e:
			pass
			data = ''

		if data=='':
			pass
			this.close()
			return 0
		this.recv_buf += data
		return len(data)

	def recv(this):
		pass

		while True:
			pass
			ret = this.parse()

			if ret==None:
				pass

				if this.net_read()==0:
					pass
					return []
			else:
				pass
				return ret

	def parse(this):
		pass
		ret = []
		spos = 0
		epos = 0

		while True:
			pass
			spos = epos
			epos = this.recv_buf.find('\n', spos)

			if epos==- (1):
				pass
				break
			epos += 1
			line = this.recv_buf[spos : epos]
			spos = epos

			if line.strip()=='':
				pass

				if len(ret)==0:
					pass
					continue
				else:
					pass
					this.recv_buf = this.recv_buf[spos : ]
					return ret
			try:
				pass
				num = int(line)
			except Exception , e:
				pass
				return []
			epos = (spos + num)

			if epos>len(this.recv_buf):
				pass
				break
			data = this.recv_buf[spos : epos]
			ret.append(data)
			spos = epos
			epos = this.recv_buf.find('\n', spos)

			if epos==- (1):
				pass
				break
			epos += 1
		return None

