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

	def add(self, filename):
		if not self.repo.untracked_files:
			pass
		index = self.repo.index
		index.add([filename])
		index.commit('Nom: adding ' + filename)

	def update(self, filename):
		if not self.is_dirty(filename):
			pass
		index = self.repo.index
		index.add([filename])
		index.commit('Nom: updating ' + filename)

	def remove(self, filename):
		index = self.repo.index
		# check to see if the file exists in the repo before removing
		index.remove([filename], r=True)
		index.commit('Nom: removing ' + filename)

	def revert(self, filename):
		if not self.is_dirty(filename):
			pass
		index = self.repo.index
		index.checkout([filename], force=True)

	def is_dirty(self, filename):
		dIndex = self.repo.index.diff(None)
		# check modified files
		for diff in dIndex.iter_change_type('M'):
			# a_blob should be locally modified files
			if filename == diff.a_blob.path:
				return True
		return False
