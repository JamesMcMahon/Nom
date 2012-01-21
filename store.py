import os
import git

# when commiting through gitpython there is an issue creating empty commits
class GitPythonStore:
	def __init__(self, cfg):
		if not os.path.exists(cfg.storeDir):
			os.makedirs(cfg.storeDir)

		if not os.path.exists(os.path.join(cfg.storeDir, '.git')):
			self.repo = git.Repo.init(cfg.storeDir)
			cw = self.repo.config_writer()
			cw.set_value('user', 'name', 'nom')
			cw.set_value('user', 'email', 'nom@github.com')
			cw.write()
		else:
			self.repo = git.Repo(cfg.storeDir)

	def add(self, file):
		if not self.repo.untracked_files:
			pass
		index = self.repo.index
		index.add([file])
		index.commit('Nom: adding ' + file)

	def update(self, file):
		# FIXME the is_dirty check isn't working as expected
		if not self.repo.is_dirty():
			pass
		index = self.repo.index
		index.add([file])
		index.commit('Nom: updating ' + file)
	
	def remove(self, file):
		index = self.repo.index
		# check to see if the file exists in the repo before removing
		index.remove([file], r=True)
		index.commit('Nom: removing ' + file)
	
	def revert(self, file):
		if not self.repo.is_dirty():
			pass
		index = self.repo.index
		index.checkout([file], force=True)

