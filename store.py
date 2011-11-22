import os
import git

class GitPythonStore:
	def __init__(self, cfg):
		if not os.path.exists(cfg.storeDir):
			os.makedirs(cfg.storeDir)

		if not os.path.exists(os.path.join(cfg.storeDir, '.git')):
			self.repo = git.Repo.init(cfg.storeDir)
		else:
			self.repo = git.Repo(cfg.storeDir)

	def add(self, file):
		if not self.repo.untracked_files:
			pass
		index = self.repo.index
		index.add([file])
		index.commit('Nom: adding ' + file)

	def update(self, file):
		if not self.repo.is_dirty():
			pass
		index = self.repo.index
		index.add([file])
		index.commit('Nom: updating ' + file)
	
	def remove(self, file):
		index = self.repo.index
		index.remove([file])
		index.commit('Nom: removing ' + file)
	
	def revert(self, file):
		if not self.repo.is_dirty():
			pass
		print 'revert not implemented yet'
		pass

