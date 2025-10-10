n = 5
for rows in range(1,n+1):
    for cols in range(1,rows+1):
        if (rows + cols) % 2 == 0: # modulo have precedence compared to + so add brackets
            print(1, end="")
        else:
            print(0, end="")
    print()

