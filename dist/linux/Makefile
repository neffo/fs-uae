version = not used

all:
	cd ../.. && fsbuild/version
	./build.py $(version)

clean:
	rm -Rf *-linux-* *-steamos-*
	rm -Rf *_linux_* *_steamos_*
	make -C ../.. clean
