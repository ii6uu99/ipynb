# Ubuntu

## About

A Ubuntu docker image tailored at my needs.


## Usage

  * Build
  
```dos
build.bat
```

  * Run. Add the directory of the file [ubuntu.cmd](ubuntu.cmd) to the `PATH` environment variable and you can call and mount the working directory everywhere.

```dos
cd /myDir
REM the cmd extension is important
REM otherwise it will start the intern windows ubuntu system
ubuntu.cmd
```


## Content

  * Binutils package (https://www.gnu.org/software/binutils/)
     * ld - linker
     * objdump - Displays information from object files.
	 * readelf - Displays information from any ELF format object file.
  * nasm assembler
