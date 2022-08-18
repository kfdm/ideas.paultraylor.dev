server: static/css/syntax.css
	hugo server --buildDrafts --buildFuture --port 1515

# https://xyproto.github.io/splash/docs/all.html
static/css/syntax.css:
	hugo gen chromastyles --style=friendly > static/css/syntax.css


.PHONY: clean
clean:
	rm static/css/syntax.css
	rm -rf public
