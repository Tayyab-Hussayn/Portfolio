<template>
  <div class="min-h-screen pt-16 bg-gray-50 flex flex-col">
    <!-- Header -->
    <div class="bg-white border-b border-gray-200 px-6 py-4">
      <div class="container-custom flex items-center justify-between">
        <div>
          <h1 class="text-2xl font-bold text-gray-900">Dotfiles & Scripts</h1>
          <p class="text-sm text-gray-500">My personal configuration files and automation scripts</p>
        </div>
        <div class="flex gap-3">
          <a 
            href="#" 
            class="hidden sm:flex items-center gap-2 px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors text-sm font-medium"
          >
            <Github class="w-4 h-4" />
            View on GitHub
          </a>
        </div>
      </div>
    </div>

    <!-- IDE Container -->
    <div class="flex-1 container-custom py-6 h-[calc(100vh-8rem)] min-h-[600px]">
      <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden flex h-full">
        <!-- Sidebar (File Explorer) -->
        <div class="w-64 bg-gray-50 border-r border-gray-200 flex flex-col">
          <div class="p-4 border-b border-gray-200">
            <h2 class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Explorer</h2>
          </div>
          <div class="flex-1 overflow-y-auto py-2">
            <div v-for="category in fileCategories" :key="category.name" class="mb-4">
              <div class="px-4 py-1 text-xs font-medium text-gray-400 flex items-center gap-1">
                <Folder class="w-3 h-3" />
                {{ category.name }}
              </div>
              <div class="mt-1">
                <button
                  v-for="file in category.files"
                  :key="file.id"
                  @click="selectFile(file)"
                  class="w-full text-left px-4 py-2 text-sm flex items-center gap-2 transition-colors border-l-2"
                  :class="selectedFile?.id === file.id ? 'bg-white border-primary text-primary font-medium' : 'border-transparent text-gray-600 hover:bg-gray-100 hover:text-gray-900'"
                >
                  <component :is="getFileIcon(file.name)" class="w-4 h-4" />
                  {{ file.name }}
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Main Code View -->
        <div class="flex-1 flex flex-col bg-[#1e1e1e] text-gray-300">
          <!-- Tab Bar -->
          <div v-if="selectedFile" class="flex items-center justify-between bg-[#252526] px-4 py-2 border-b border-[#333]">
            <div class="flex items-center gap-2 text-sm text-gray-100">
              <component :is="getFileIcon(selectedFile.name)" class="w-4 h-4 text-blue-400" />
              {{ selectedFile.name }}
            </div>
            <div class="flex items-center gap-2">
              <button 
                @click="copyContent"
                class="p-1.5 hover:bg-[#333] rounded-md text-gray-400 hover:text-white transition-colors"
                title="Copy Content"
              >
                <Copy class="w-4 h-4" />
              </button>
              <button 
                class="p-1.5 hover:bg-[#333] rounded-md text-gray-400 hover:text-white transition-colors"
                title="Download"
              >
                <Download class="w-4 h-4" />
              </button>
            </div>
          </div>

          <!-- Code Content -->
          <div v-if="selectedFile" class="flex-1 overflow-auto p-6 font-mono text-sm leading-relaxed">
            <pre><code class="language-bash">{{ selectedFile.content }}</code></pre>
          </div>

          <!-- Empty State -->
          <div v-else class="flex-1 flex flex-col items-center justify-center text-gray-500">
            <FileCode class="w-16 h-16 mb-4 opacity-20" />
            <p>Select a file to view its content</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Github, Folder, FileCode, FileJson, FileText, Terminal, Copy, Download } from 'lucide-vue-next'

export default {
  name: 'Dotfiles',
  components: {
    Github,
    Folder,
    FileCode,
    FileJson,
    FileText,
    Terminal,
    Copy,
    Download
  },
  data() {
    return {
      selectedFile: null,
      fileCategories: [
        {
          name: 'Shell',
          files: [
            {
              id: 'zshrc',
              name: '.zshrc',
              content: `# Oh My Zsh Configuration
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="spaceship"
plugins=(git docker npm python)

source $ZSH/oh-my-zsh.sh

# Aliases
alias g="git"
alias d="docker"
alias k="kubectl"
alias dev="cd ~/projects"
alias ..="cd .."
alias ...="cd ../.."

# Environment
export EDITOR="code"
export NODE_ENV="development"
export PATH="$HOME/bin:$PATH"`
            },
            {
              id: 'bash_profile',
              name: '.bash_profile',
              content: `# Bash Profile
if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi

# User specific environment and startup programs
export PATH=$PATH:$HOME/.local/bin:$HOME/bin`
            }
          ]
        },
        {
          name: 'Git',
          files: [
            {
              id: 'gitconfig',
              name: '.gitconfig',
              content: `[user]
  name = Krawin
  email = krawin@example.com

[core]
  editor = code --wait
  excludesfile = ~/.gitignore_global

[alias]
  co = checkout
  br = branch
  ci = commit
  st = status
  unstage = reset HEAD --
  last = log -1 HEAD

[color]
  ui = auto`
            },
            {
              id: 'gitignore',
              name: '.gitignore_global',
              content: `# MacOS
.DS_Store

# Node
node_modules
npm-debug.log

# Python
__pycache__
*.pyc

# IDEs
.vscode
.idea`
            }
          ]
        },
        {
          name: 'Scripts',
          files: [
            {
              id: 'setup',
              name: 'setup.sh',
              content: `#!/bin/bash

# System Setup Script

echo "Starting setup..."

# Install Homebrew
if ! command -v brew &> /dev/null; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Dependencies
brew install node python git zsh

# Setup Zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

echo "Setup complete! 🚀"`
            }
          ]
        }
      ]
    }
  },
  created() {
    // Select first file by default
    if (this.fileCategories[0]?.files[0]) {
      this.selectedFile = this.fileCategories[0].files[0]
    }
  },
  methods: {
    selectFile(file) {
      this.selectedFile = file
    },
    getFileIcon(filename) {
      if (filename.endsWith('.sh') || filename.includes('rc')) return 'Terminal'
      if (filename.endsWith('.json')) return 'FileJson'
      if (filename.includes('git')) return 'Github'
      return 'FileText'
    },
    async copyContent() {
      if (!this.selectedFile) return
      try {
        await navigator.clipboard.writeText(this.selectedFile.content)
        alert('Content copied to clipboard!')
      } catch (err) {
        console.error('Failed to copy:', err)
      }
    }
  }
}
</script>
