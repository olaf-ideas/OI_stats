for numer in {1..29}; do
	for etap in {1..3}; do
		echo -n "DOWNLOADING OI${numer} etap${etap} $((numer+1993)): "
		python3 fetch_data.py $numer $etap
		echo "done"
	done
done
