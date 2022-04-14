for ((numer = 29; numer >= 19; numer--)); do
	for ((etap = 1; etap <= 3; etap++)); do
		echo -n "DOWNLOADING OI${numer} etap${etap} $((numer+1993)): "
		python3 fetch_data.py $numer $etap
		echo "done"
	done
done
