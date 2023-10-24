package main

import "C"
import "golang.org/x/text/width"

func main() {}

//export Widen
func Widen(s *C.char) *C.char {
	return C.CString(width.Widen.String(C.GoString(s)))
}

//export Narrow
func Narrow(s *C.char) *C.char {
	return C.CString(width.Narrow.String(C.GoString(s)))
}

//export Fold
func Fold(s *C.char) *C.char {
	return C.CString(width.Fold.String(C.GoString(s)))
}
