alias nano='micro'
alias ssh='xxh'
alias c='clear'
function up {
       if [[ "$#" < 1 ]] ; then
           cd ..
   	   else
           CDSTR=""
           for i in {1..$1} ; do
               CDSTR="../$CDSTR"
           done
           cd $CDSTR
       fi
}
function cf {
	pbcopy < $1
	echo "Copied file contents"
}
alias g="git"
alias ..='cd ..'
alias ...='cd ../..'
alias ls='exa'
alias cat='bat'
function $ {
	$1
}
